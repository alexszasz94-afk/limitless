import { checkAllKeys } from "./apify/keys";
import { type Db, getMeta, setMeta } from "./db";

/**
 * Checks every Apify key and stores the result for the Keys page: the summary
 * in meta "key_pool", the per-key list in meta "key_pool_keys". Run by the
 * scraper every cycle and by the Keys page's "Check now" button.
 */
export async function refreshKeyPool(db: Db): Promise<void> {
  const { summary, keys } = await checkAllKeys();
  setMeta(db, "key_pool", JSON.stringify(summary));
  setMeta(db, "key_pool_keys", JSON.stringify(keys));
}

/** Seconds since the last key check (Infinity if never). */
export function keyPoolAgeSeconds(db: Db): number {
  const raw = getMeta(db, "key_pool");
  if (!raw) return Infinity;
  return (Date.now() - Date.parse((JSON.parse(raw) as { checkedAt: string }).checkedAt)) / 1000;
}
