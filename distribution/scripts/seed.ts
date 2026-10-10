/**
 * DEMO seed for a local test database: loads the demo personas from
 * seed-assets/demo_personas.json, creates one poster per persona with an
 * unguessable token, and registers placeholder content from seed-assets/ so
 * the app is fully clickable on first run. Real personas are loaded with
 * `npm run manage -- import <persona>` instead (scripts/manage.ts).
 *
 * It WIPES every row. To protect a live portal it refuses to run once the
 * database holds any poster progress or any real (non-demo) persona, unless
 * called with --force.
 *
 *   npm run seed            # fresh / demo database only
 *   npm run seed -- --force # wipe real progress too (never on the live app)
 */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { db, hasAnyProgress } from "../lib/db";
import { platformIds, type PersonaSeed } from "../lib/config";

const ROOT = process.cwd();
const CONTENT = path.resolve(process.env.CONTENT_DIR ?? path.join(ROOT, "content"));
const SEED_ASSETS = path.join(ROOT, "seed-assets");
const force = process.argv.includes("--force");

const { personas } = JSON.parse(
  fs.readFileSync(path.join(SEED_ASSETS, "demo_personas.json"), "utf8"),
) as { personas: PersonaSeed[] };

const demoIds = new Set(personas.map((p) => p.id));
const realPersonas = (db().prepare("SELECT id FROM personas").all() as Array<{ id: string }>)
  .map((r) => r.id)
  .filter((id) => !demoIds.has(id));

if ((hasAnyProgress() || realPersonas.length > 0) && !force) {
  console.error(
    "Refusing to seed: the database already holds " +
      (realPersonas.length ? `real personas (${realPersonas.join(", ")})` : "poster progress") +
      ".\nSeeding wipes everything. If you really mean it: npm run seed -- --force",
  );
  process.exit(1);
}

function token(): string {
  return crypto.randomBytes(12).toString("base64url"); // 16 url-safe chars, 96 bits
}

function copyAsset(src: string, destRel: string): string {
  const dest = path.join(CONTENT, destRel);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.copyFileSync(path.join(SEED_ASSETS, src), dest);
  return destRel.split(path.sep).join("/");
}

const d = db();
const platforms = platformIds();
const posterNames = ["Alex", "Bella", "Chris", "Dana", "Eli", "Fiona"];
const TIMEZONE = process.env.TIMEZONE || "UTC";
// Start date in the posters' own timezone (the day counter uses the same zone).
const today = new Intl.DateTimeFormat("en-CA", { timeZone: TIMEZONE }).format(new Date());

const captions = (text: string) =>
  JSON.stringify(Object.fromEntries(platforms.map((p) => [p, text.replace("{p}", p)])));

const urls: string[] = [];

d.transaction(() => {
  d.exec(`
    DELETE FROM post_log; DELETE FROM progress; DELETE FROM assignments;
    DELETE FROM day_opens; DELETE FROM content_items; DELETE FROM posters;
    DELETE FROM personas;
  `);

  const insertPersona = d.prepare(`
    INSERT INTO personas (id, name, handles_json, bio, profile_image_path,
      cover_image_path, competitors_json, keywords_json, voice_notes, pinned_comment)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`);
  const insertPoster = d.prepare(`
    INSERT INTO posters (id, name, token, persona_id, start_date, timezone)
    VALUES (?, ?, ?, ?, ?, ?)`);
  const insertContent = d.prepare(`
    INSERT INTO content_items (id, persona_id, kind, master_path, proxy_path,
      source_clip_id, duration_seconds, captions_json, queue_order, status, variants_json)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'queued', ?)`);

  personas.forEach((p, pi) => {
    const missing = platforms.filter((id) => !p.handles[id]);
    if (missing.length) console.warn(`  ! ${p.id} has no handle for: ${missing.join(", ")}`);

    const n = (pi % 3) + 1;
    const profile = copyAsset(`profile_${n}.jpg`, `${p.id}/images/profile.jpg`);
    const cover = copyAsset(`cover_${n}.jpg`, `${p.id}/images/cover.jpg`);
    insertPersona.run(
      p.id,
      p.name,
      JSON.stringify(p.handles),
      p.bio,
      profile,
      cover,
      JSON.stringify(p.competitors),
      JSON.stringify(p.keywords),
      p.voice_notes ?? "",
      p.pinned_comment ?? "",
    );

    const t = token();
    const name = posterNames[pi] ?? `Poster ${pi + 1}`;
    insertPoster.run(`poster_${pi + 1}`, name, t, p.id, today, TIMEZONE);
    urls.push(`  ${name.padEnd(8)} /d/${t}   (${p.name})`);

    // 12 reels cycling 4 sample videos; clip ids repeat so the clip-spacing
    // rule is exercised. The FIRST persona gets a Facebook variant on every
    // reel (a different file) to exercise per-platform videos.
    for (let i = 0; i < 12; i++) {
      const vid = (i % 4) + 1;
      const master = copyAsset(`reel_${vid}.mp4`, `${p.id}/reels/master_${i + 1}.mp4`);
      const proxy = copyAsset(`reel_${vid}_proxy.mp4`, `${p.id}/reels/proxy_${i + 1}.mp4`);
      let variants = "{}";
      if (pi === 0 && platforms.includes("facebook")) {
        const fb = (vid % 4) + 1;
        variants = JSON.stringify({
          facebook: {
            master_path: copyAsset(`reel_${fb}.mp4`, `${p.id}/reels/master_${i + 1}_fb.mp4`),
            proxy_path: copyAsset(`reel_${fb}_proxy.mp4`, `${p.id}/reels/proxy_${i + 1}_fb.mp4`),
          },
        });
      }
      insertContent.run(
        `${p.id}_reel_${i + 1}`,
        p.id,
        "reel",
        master,
        proxy,
        `clip_${vid}`,
        5,
        captions(`Sample caption ${i + 1} for {p}. Replace with the real caption ✨ #fyp`),
        i + 1,
        variants,
      );
    }

    for (let i = 0; i < 4; i++) {
      const vid = (i % 4) + 1;
      insertContent.run(
        `${p.id}_story_${i + 1}`,
        p.id,
        "story",
        copyAsset(`reel_${vid}.mp4`, `${p.id}/stories/master_${i + 1}.mp4`),
        copyAsset(`reel_${vid}_proxy.mp4`, `${p.id}/stories/proxy_${i + 1}.mp4`),
        `clip_${vid}`,
        5,
        captions(""),
        i + 1,
        "{}",
      );
    }

    for (let i = 0; i < 3; i++) {
      const img = copyAsset(`highlight_${(i % 2) + 1}.jpg`, `${p.id}/highlights/cover_${i + 1}.jpg`);
      insertContent.run(
        `${p.id}_hl_${i + 1}`,
        p.id,
        "highlight_cover",
        img,
        img, // images: proxy = master, no transformation either way
        null,
        null,
        JSON.stringify({ instagram: "Add this as the cover of a new highlight." }),
        i + 1,
        "{}",
      );
    }
  });
})();

console.log(`Seeded ${personas.length} personas, ${personas.length} posters, sample content.\n`);
console.log("Poster links (open on http://localhost:3000):");
for (const u of urls) console.log(u);
console.log("\nAdmin: /admin (passphrase = ADMIN_PASSPHRASE in .env)");
