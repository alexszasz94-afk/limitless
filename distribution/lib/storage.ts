/**
 * Storage adapter — local disk under /content.
 *
 * SWAP POINT: to move to S3/R2 later, reimplement `openReadStream`,
 * `statFile` and `resolveSafe` against your object store (e.g. return
 * signed URLs or proxy streams). Nothing outside this file touches the
 * filesystem for content bytes.
 *
 * Masters are a dumb byte bucket: nothing in this module (or anywhere
 * else) may transform file contents. Bytes in = bytes out.
 */
import fs from "node:fs";
import path from "node:path";

const CONTENT_ROOT = path.resolve(
  /*turbopackIgnore: true*/ process.env.CONTENT_DIR ?? path.join(/*turbopackIgnore: true*/ process.cwd(), "content"),
);

export function contentRoot(): string {
  return CONTENT_ROOT;
}

/** Resolve a relative content path, refusing anything that escapes the root. */
export function resolveSafe(relPath: string): string {
  const abs = path.resolve(CONTENT_ROOT, relPath);
  if (!abs.startsWith(CONTENT_ROOT + path.sep) && abs !== CONTENT_ROOT) {
    throw new Error("Path escapes content root");
  }
  return abs;
}

export function statFile(relPath: string): fs.Stats | null {
  try {
    return fs.statSync(resolveSafe(relPath));
  } catch {
    return null;
  }
}

export function openReadStream(
  relPath: string,
  range?: { start: number; end: number },
): fs.ReadStream {
  return fs.createReadStream(resolveSafe(relPath), range);
}

export function mimeFor(relPath: string): string {
  const ext = path.extname(relPath).toLowerCase();
  switch (ext) {
    case ".mp4": return "video/mp4";
    case ".mov": return "video/quicktime";
    case ".webm": return "video/webm";
    case ".jpg":
    case ".jpeg": return "image/jpeg";
    case ".png": return "image/png";
    case ".webp": return "image/webp";
    default: return "application/octet-stream";
  }
}
