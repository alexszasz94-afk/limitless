import { loadProducts } from "./config";
import { type Db, upsertAccount, upsertProduct } from "./db";

/**
 * config/products.json is the source of truth for products and accounts.
 * A new product or account is picked up on the next cycle; an account that
 * disappears from the file is paused (never deleted: its history stays).
 */
export function syncConfigToDb(db: Db): void {
  const products = loadProducts();
  db.transaction(() => {
    const seen = new Set<number>();
    products.forEach((p, i) => {
      upsertProduct(db, { id: p.id, name: p.name, active: p.active, avatar: p.avatar ?? null, sort: i });
      for (const a of p.accounts ?? []) {
        seen.add(
          upsertAccount(db, {
            productId: p.id,
            platform: a.platform,
            handle: a.handle.trim(),
            url: a.url.trim(),
            active: a.active && p.active,
          }),
        );
      }
    });
    const productIds = new Set(products.map((p) => p.id));
    for (const row of db.prepare(`SELECT id FROM accounts`).all() as Array<{ id: number }>) {
      if (!seen.has(row.id)) db.prepare(`UPDATE accounts SET active=0 WHERE id=?`).run(row.id);
    }
    for (const row of db.prepare(`SELECT id FROM products`).all() as Array<{ id: string }>) {
      if (!productIds.has(row.id)) db.prepare(`UPDATE products SET active=0 WHERE id=?`).run(row.id);
    }
  })();
}
