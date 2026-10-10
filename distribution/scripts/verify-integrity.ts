/**
 * Integrity proof: hashes a source file and a downloaded file and confirms
 * byte-identity. This is how we PROVE the master pipeline never modifies
 * a render, rather than asserting it.
 *
 * Usage:
 *   npm run verify-integrity -- <source-file> <downloaded-file>
 *
 * Or with a running server, verify end-to-end over HTTP:
 *   npm run verify-integrity -- <source-file> --url http://localhost:3000/api/media/<token>/master/<contentId>
 */
import fs from "node:fs";
import crypto from "node:crypto";

function sha256File(p: string): string {
  const h = crypto.createHash("sha256");
  h.update(fs.readFileSync(p));
  return h.digest("hex");
}

async function sha256Url(url: string): Promise<{ hash: string; bytes: number }> {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status} from ${url}`);
  const buf = Buffer.from(await res.arrayBuffer());
  const h = crypto.createHash("sha256");
  h.update(buf);
  return { hash: h.digest("hex"), bytes: buf.length };
}

async function main() {
  const args = process.argv.slice(2);
  if (args.length < 2) {
    console.error(
      "Usage: verify-integrity <source> <downloaded>  OR  <source> --url <master-url>",
    );
    process.exit(2);
  }

  const source = args[0];
  const srcHash = sha256File(source);
  const srcBytes = fs.statSync(source).size;

  let dlHash: string;
  let dlBytes: number;
  if (args[1] === "--url") {
    const r = await sha256Url(args[2]);
    dlHash = r.hash;
    dlBytes = r.bytes;
  } else {
    dlHash = sha256File(args[1]);
    dlBytes = fs.statSync(args[1]).size;
  }

  console.log(`source     sha256=${srcHash}  (${srcBytes} bytes)`);
  console.log(`downloaded sha256=${dlHash}  (${dlBytes} bytes)`);

  if (srcHash === dlHash) {
    console.log("MATCH — downloaded file is byte-identical to the source.");
  } else {
    console.error("MISMATCH — the pipeline modified the file. This is a bug.");
    process.exit(1);
  }
}

main();
