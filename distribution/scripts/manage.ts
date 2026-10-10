/**
 * Manage the real portal data without wiping anything (the demo seed wipes;
 * this never does). Safe to run on the live server:
 *
 *   npm run manage -- list
 *   npm run manage -- import <persona>          persona from config/personas.json +
 *                                               content from content-manifests/<persona>.json
 *   npm run manage -- add-poster <persona> "<name>"
 *   npm run manage -- remove-persona <persona> [--force]
 *   npm run manage -- reset-poster <token>       back to day 1, start date today; videos
 *                                               handed to them go back to the queue
 *
 * On the server: docker compose exec app npm run manage -- <command>
 *
 * import is idempotent: the manifest order is the posting order (re-applied on
 * every import, so reordering the manifest reorders the videos still queued);
 * existing items get their caption/files/duration updated (status and progress
 * are never touched); items missing from the manifest are only reported.
 * Every file is checked to exist (and be non-empty) BEFORE anything is
 * written, so a half-uploaded content folder never reaches a poster.
 */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { db } from "../lib/db";
import { getPersonasConfig, platformIds } from "../lib/config";
import { contentRoot, statFile } from "../lib/storage";

// The posters' timezone (decides when a "day" starts): TIMEZONE in .env, e.g. Europe/London.
const TIMEZONE = process.env.TIMEZONE || "UTC";
const KINDS = new Set(["reel", "story", "highlight_cover"]);

interface ManifestItem {
  id: string;
  kind: string;
  master: string;
  proxy: string;
  duration_seconds?: number;
  caption: string | Record<string, string>;
  clip?: string;
}
interface Manifest {
  persona: string;
  profile_image: string;
  cover_image: string;
  items: ManifestItem[];
}

function fail(msg: string): never {
  console.error(`\n✗ ${msg}`);
  process.exit(1);
}

function rel(persona: string, p: string): string {
  return `${persona}/${p}`.split(path.sep).join("/");
}

function requireFile(relPath: string, problems: string[]) {
  const st = statFile(relPath);
  if (!st || !st.isFile()) problems.push(`missing: ${relPath}`);
  else if (st.size === 0) problems.push(`empty: ${relPath}`);
}

function list() {
  const d = db();
  const personas = d.prepare("SELECT id, name FROM personas ORDER BY id").all() as Array<{ id: string; name: string }>;
  if (!personas.length) console.log("No personas.");
  for (const p of personas) {
    const q = d
      .prepare("SELECT status, COUNT(*) n FROM content_items WHERE persona_id = ? GROUP BY status")
      .all(p.id) as Array<{ status: string; n: number }>;
    console.log(`\n${p.name} (${p.id})  content: ${q.map((r) => `${r.n} ${r.status}`).join(", ") || "none"}`);
    const posters = d.prepare("SELECT name, token, start_date FROM posters WHERE persona_id = ? ORDER BY name").all(p.id) as Array<{
      name: string;
      token: string;
      start_date: string;
    }>;
    for (const r of posters) console.log(`  ${r.name.padEnd(22)} /d/${r.token}   started ${r.start_date}`);
  }
}

function importPersona(id: string) {
  const persona = getPersonasConfig().personas.find((p) => p.id === id);
  if (!persona) fail(`No persona "${id}" in config/personas.json`);

  const manifestFile = path.join(process.cwd(), "content-manifests", `${id}.json`);
  if (!fs.existsSync(manifestFile)) fail(`No manifest at content-manifests/${id}.json`);
  const m = JSON.parse(fs.readFileSync(manifestFile, "utf8")) as Manifest;
  if (m.persona !== id) fail(`Manifest is for "${m.persona}", not "${id}"`);

  const platforms = platformIds();
  const problems: string[] = [];
  const missingHandles = platforms.filter((p) => !persona.handles[p]);
  if (missingHandles.length) problems.push(`no handle for: ${missingHandles.join(", ")}`);
  requireFile(rel(id, m.profile_image), problems);
  requireFile(rel(id, m.cover_image), problems);
  const seen = new Set<string>();
  for (const it of m.items) {
    if (!/^[a-zA-Z0-9_-]+$/.test(it.id)) problems.push(`bad id: ${it.id}`);
    if (seen.has(it.id)) problems.push(`duplicate id: ${it.id}`);
    seen.add(it.id);
    if (!KINDS.has(it.kind)) problems.push(`${it.id}: unknown kind ${it.kind}`);
    requireFile(rel(id, it.master), problems);
    requireFile(rel(id, it.proxy), problems);
    if (typeof it.caption === "object") {
      const extra = Object.keys(it.caption).filter((k) => !platforms.includes(k));
      if (extra.length) problems.push(`${it.id}: caption for unknown platform ${extra.join(", ")}`);
    }
  }
  if (problems.length) fail(`Nothing imported. Fix these first (content folder: ${contentRoot()}):\n  ${problems.join("\n  ")}`);

  const d = db();
  let added = 0;
  let updated = 0;
  d.transaction(() => {
    d.prepare(
      `INSERT INTO personas (id, name, handles_json, bio, profile_image_path, cover_image_path,
         competitors_json, keywords_json, voice_notes, pinned_comment)
       VALUES (@id, @name, @handles, @bio, @profile, @cover, @competitors, @keywords, @voice, @pinned)
       ON CONFLICT (id) DO UPDATE SET name = excluded.name, handles_json = excluded.handles_json,
         bio = excluded.bio, profile_image_path = excluded.profile_image_path,
         cover_image_path = excluded.cover_image_path, competitors_json = excluded.competitors_json,
         keywords_json = excluded.keywords_json, voice_notes = excluded.voice_notes,
         pinned_comment = excluded.pinned_comment`,
    ).run({
      id,
      name: persona.name,
      handles: JSON.stringify(persona.handles),
      bio: persona.bio,
      profile: rel(id, m.profile_image),
      cover: rel(id, m.cover_image),
      competitors: JSON.stringify(persona.competitors ?? []),
      keywords: JSON.stringify(persona.keywords ?? []),
      voice: persona.voice_notes ?? "",
      pinned: persona.pinned_comment ?? "",
    });

    const exists = d.prepare("SELECT 1 FROM content_items WHERE id = ?");
    let order = 0; // manifest position = posting order
    const insert = d.prepare(
      `INSERT INTO content_items (id, persona_id, kind, master_path, proxy_path, source_clip_id,
         duration_seconds, captions_json, queue_order, status, variants_json)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'queued', '{}')`,
    );
    const update = d.prepare(
      `UPDATE content_items SET master_path = ?, proxy_path = ?, source_clip_id = ?,
         duration_seconds = ?, captions_json = ?, queue_order = ? WHERE id = ?`,
    );
    for (const it of m.items) {
      const itemId = `${id}_${it.id}`;
      const captions =
        typeof it.caption === "string"
          ? Object.fromEntries(platforms.map((p) => [p, it.caption as string]))
          : it.caption;
      const args = [
        rel(id, it.master),
        rel(id, it.proxy),
        it.clip ?? it.id,
        it.duration_seconds ?? null,
        JSON.stringify(captions),
      ] as const;
      order++;
      if (exists.get(itemId)) {
        update.run(...args, order, itemId);
        updated++;
      } else {
        insert.run(itemId, id, it.kind, args[0], args[1], args[2], args[3], args[4], order);
        added++;
      }
    }
  })();

  const inManifest = new Set(m.items.map((it) => `${id}_${it.id}`));
  const extra = (d.prepare("SELECT id FROM content_items WHERE persona_id = ?").all(id) as Array<{ id: string }>)
    .map((r) => r.id)
    .filter((x) => !inManifest.has(x));
  console.log(`✓ ${persona.name}: persona saved, ${added} new item(s) queued, ${updated} updated.`);
  if (extra.length) console.log(`  Note: in the database but not in the manifest (left as they are): ${extra.join(", ")}`);
}

function addPoster(personaId: string, name: string) {
  const d = db();
  if (!d.prepare("SELECT 1 FROM personas WHERE id = ?").get(personaId)) fail(`No persona "${personaId}" (import it first)`);
  if (!name?.trim()) fail("Give the poster a name");
  const token = crypto.randomBytes(12).toString("base64url"); // 16 url-safe chars, 96 bits
  const n = (d.prepare("SELECT COUNT(*) AS n FROM posters").get() as { n: number }).n;
  let pid = `poster_${n + 1}`;
  while (d.prepare("SELECT 1 FROM posters WHERE id = ?").get(pid)) pid = `poster_${crypto.randomBytes(3).toString("hex")}`;
  const today = new Intl.DateTimeFormat("en-CA", { timeZone: TIMEZONE }).format(new Date());
  d.prepare("INSERT INTO posters (id, name, token, persona_id, start_date, timezone) VALUES (?, ?, ?, ?, ?, ?)").run(
    pid,
    name.trim(),
    token,
    personaId,
    today,
    TIMEZONE,
  );
  console.log(`✓ Poster "${name.trim()}" for ${personaId}: /d/${token}`);
}

function removePersona(personaId: string, force: boolean) {
  const d = db();
  if (!d.prepare("SELECT 1 FROM personas WHERE id = ?").get(personaId)) fail(`No persona "${personaId}"`);
  const posters = (d.prepare("SELECT id FROM posters WHERE persona_id = ?").all(personaId) as Array<{ id: string }>).map(
    (r) => r.id,
  );
  const ph = posters.map(() => "?").join(",") || "NULL";
  const work = (
    d
      .prepare(
        `SELECT (SELECT COUNT(*) FROM progress WHERE poster_id IN (${ph})) +
                (SELECT COUNT(*) FROM post_log WHERE poster_id IN (${ph})) AS n`,
      )
      .get(...posters, ...posters) as { n: number }
  ).n;
  if (work > 0 && !force) fail(`${personaId} has ${work} progress/post rows. Add --force to delete them too.`);
  d.transaction(() => {
    for (const t of ["post_log", "progress", "assignments", "day_opens"]) {
      d.prepare(`DELETE FROM ${t} WHERE poster_id IN (${ph})`).run(...posters);
    }
    d.prepare("DELETE FROM posters WHERE persona_id = ?").run(personaId);
    d.prepare("DELETE FROM content_items WHERE persona_id = ?").run(personaId);
    d.prepare("DELETE FROM personas WHERE id = ?").run(personaId);
  })();
  console.log(`✓ Removed ${personaId} and its ${posters.length} poster(s). Files in the content folder were left alone.`);
}

function resetPoster(token: string) {
  const d = db();
  const p = d.prepare("SELECT id, name FROM posters WHERE token = ?").get(token) as { id: string; name: string } | undefined;
  if (!p) fail(`No poster with token ${token}`);
  const today = new Intl.DateTimeFormat("en-CA", { timeZone: TIMEZONE }).format(new Date());
  let freed = 0;
  d.transaction(() => {
    // Videos handed to this poster (and not to anyone else) go back to the front of the queue.
    freed = d
      .prepare(
        `UPDATE content_items SET status = 'queued'
         WHERE id IN (SELECT content_item_id FROM assignments WHERE poster_id = ? AND content_item_id IS NOT NULL)
           AND id NOT IN (SELECT content_item_id FROM assignments WHERE poster_id != ? AND content_item_id IS NOT NULL)`,
      )
      .run(p.id, p.id).changes;
    for (const t of ["post_log", "progress", "assignments", "day_opens"]) {
      d.prepare(`DELETE FROM ${t} WHERE poster_id = ?`).run(p.id);
    }
    d.prepare("UPDATE posters SET start_date = ? WHERE id = ?").run(today, p.id);
  })();
  console.log(`✓ ${p.name} is back on day 1 (start date ${today}); ${freed} video(s) back in the queue. Same link.`);
}

const [cmd, ...args] = process.argv.slice(2);
const force = args.includes("--force");
const pos = args.filter((a) => a !== "--force");
switch (cmd) {
  case "list":
    list();
    break;
  case "import":
    if (!pos[0]) fail("Usage: import <persona>");
    importPersona(pos[0]);
    break;
  case "add-poster":
    if (!pos[0] || !pos[1]) fail('Usage: add-poster <persona> "<name>"');
    addPoster(pos[0], pos.slice(1).join(" "));
    break;
  case "remove-persona":
    if (!pos[0]) fail("Usage: remove-persona <persona> [--force]");
    removePersona(pos[0], force);
    break;
  case "reset-poster":
    if (!pos[0]) fail("Usage: reset-poster <token>");
    resetPoster(pos[0]);
    break;
  default:
    console.log(
      "Commands: list | import <persona> | add-poster <persona> \"<name>\" | remove-persona <persona> [--force] | reset-poster <token>",
    );
}
