/**
 * Media endpoint.
 *   /api/media/:token/master/:contentId  -> original bytes, attachment, range OK
 *   /api/media/:token/proxy/:contentId   -> low-res preview stream
 *   /api/media/:token/profile/:personaId -> persona profile image
 *   /api/media/:token/cover/:personaId   -> persona cover image
 *     (?preview=1 serves a small <name>.preview.jpg thumbnail when present,
 *      ?download=1 the original as an attachment)
 *
 * Masters stream the ORIGINAL bytes with Content-Disposition: attachment.
 * No transcoding, no transformation, ever (`no-transform` also tells any
 * proxy in front not to touch them). Range requests are supported so phone
 * downloads can resume.
 */
import { NextRequest } from "next/server";
import { Readable } from "node:stream";
import path from "node:path";
import { cookies } from "next/headers";
import { getPosterByToken, getContentItem, getPersona, isAssignedTo } from "@/lib/db";
import { statFile, openReadStream, mimeFor } from "@/lib/storage";
import { isAdminSession } from "@/lib/admin";

const notFound = () => new Response("Not found", { status: 404 });

function safeName(s: string): string {
  return s.replace(/[^a-zA-Z0-9._-]+/g, "_").slice(0, 120) || "file";
}

export async function GET(
  req: NextRequest,
  { params }: { params: Promise<{ token: string; kind: string; id: string }> },
) {
  const { token, kind, id } = await params;

  const poster = getPosterByToken(token);
  // The admin dashboard may fetch media too (token "admin" + admin cookie).
  const admin = !poster && token === "admin" && isAdminSession(await cookies());
  if (!poster && !admin) return notFound();

  let relPath: string;
  let asAttachment = false;
  let filename: string;

  if (kind === "master" || kind === "proxy") {
    const item = getContentItem(id);
    if (!item) return notFound();
    // Posters only ever reach content that was handed to them.
    if (poster && (item.persona_id !== poster.persona_id || !isAssignedTo(poster.id, item.id))) {
      return notFound();
    }
    // Optional per-platform file override (?platform=facebook). The variant
    // is its own original file; the same no-transcoding rule applies.
    const platform = req.nextUrl.searchParams.get("platform");
    const variant =
      platform && item.variants && Object.prototype.hasOwnProperty.call(item.variants, platform)
        ? item.variants[platform]
        : undefined;
    relPath = variant
      ? kind === "master" ? variant.master_path : variant.proxy_path
      : kind === "master" ? item.master_path : item.proxy_path;
    asAttachment = kind === "master";
    filename = `${item.kind}_${item.id}${variant ? `_${platform}` : ""}${path.extname(relPath)}`;
  } else if (kind === "profile" || kind === "cover") {
    const persona = getPersona(id);
    if (!persona) return notFound();
    if (poster && persona.id !== poster.persona_id) return notFound();
    relPath = kind === "profile" ? persona.profile_image_path : persona.cover_image_path;
    asAttachment = req.nextUrl.searchParams.get("download") === "1";
    filename = `${persona.name}_${kind}${path.extname(relPath)}`;
    // On-screen thumbnail: a small "<name>.preview.jpg" next to the original,
    // when there is one. Saving (?download=1 or share) always gets the original.
    if (!asAttachment && req.nextUrl.searchParams.get("preview") === "1" && relPath) {
      const preview = relPath.replace(/\.[^./]+$/, "") + ".preview.jpg";
      if (statFile(preview)) relPath = preview;
    }
  } else {
    return notFound();
  }

  const stat = relPath ? statFile(relPath) : null;
  if (!relPath || !stat) return new Response("File missing", { status: 404 });

  const size = stat.size;
  const headers: Record<string, string> = {
    "Content-Type": mimeFor(relPath),
    "Accept-Ranges": "bytes",
    "Cache-Control": "private, max-age=3600, no-transform",
    "Last-Modified": stat.mtime.toUTCString(),
    "X-Content-Type-Options": "nosniff",
  };
  if (asAttachment) {
    headers["Content-Disposition"] = `attachment; filename="${safeName(filename)}"`;
  }

  const rangeHeader = req.headers.get("range");
  const m = rangeHeader ? /^bytes=(\d*)-(\d*)$/.exec(rangeHeader.trim()) : null;
  if (m && (m[1] !== "" || m[2] !== "")) {
    let start: number;
    let end: number;
    if (m[1] === "") {
      // suffix range: the last N bytes
      start = Math.max(0, size - parseInt(m[2], 10));
      end = size - 1;
    } else {
      start = parseInt(m[1], 10);
      end = m[2] === "" ? size - 1 : Math.min(parseInt(m[2], 10), size - 1);
    }
    if (start >= size || start > end) {
      return new Response(null, { status: 416, headers: { "Content-Range": `bytes */${size}` } });
    }
    const stream = openReadStream(relPath, { start, end });
    return new Response(Readable.toWeb(stream) as ReadableStream, {
      status: 206,
      headers: {
        ...headers,
        "Content-Range": `bytes ${start}-${end}/${size}`,
        "Content-Length": String(end - start + 1),
      },
    });
  }

  const stream = openReadStream(relPath);
  return new Response(Readable.toWeb(stream) as ReadableStream, {
    status: 200,
    headers: { ...headers, "Content-Length": String(size) },
  });
}
