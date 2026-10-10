import Link from "next/link";
import type { Metadata } from "next";
import Shell from "@/components/Shell";
import SelectNav from "@/components/SelectNav";
import { PlatformDot } from "@/components/platform";
import { Card, Chips, Empty, ExternalIcon, N, PageHeader } from "@/components/ui";
import { PLATFORMS, PLATFORM_LABEL, isPlatform } from "@/lib/config";
import { getDb } from "@/lib/db";
import { fmtAge, fmtDateTime, fmtHandle } from "@/lib/format";
import {
  PAGE_SIZE,
  PERIODS,
  PERIOD_LABEL,
  POST_SORTS,
  type PostSort,
  listProducts,
  parsePeriod,
  parseProduct,
  posts,
} from "@/lib/queries";
import { requireSignIn } from "@/lib/session";
import { flatParams, hrefWith } from "@/lib/url";

export const dynamic = "force-dynamic";
export const metadata: Metadata = { title: "Videos" };

const pctFmt = (v: number | null) => (v === null ? "–" : `${(v * 100).toFixed(v < 0.1 ? 1 : 0)}%`);

export default async function VideosPage({
  searchParams,
}: {
  searchParams: Promise<Record<string, string | string[] | undefined>>;
}) {
  await requireSignIn();
  const sp = flatParams(await searchParams);
  const db = getDb();
  const productId = parseProduct(db, sp.product);
  const period = parsePeriod(sp.period);
  const platform = isPlatform(sp.platform) ? sp.platform : null;
  const sort: PostSort = POST_SORTS.some((s) => s.id === sp.sort) ? (sp.sort as PostSort) : "period";
  const page = Math.min(100_000, Math.max(1, Math.floor(Number(sp.page) || 1)));
  const products = listProducts(db).filter((p) => p.active || p.id === productId);
  const { rows, total } = posts({ productId, platform, sort, period, page });
  const pages = Math.max(1, Math.ceil(total / PAGE_SIZE));
  const showProduct = !productId && products.length > 1;
  const periodCol = period === "all" ? "Gained" : PERIOD_LABEL[period];

  return (
    <Shell>
      <PageHeader
        title="Videos"
        sub={`${total} video${total === 1 ? "" : "s"}${platform ? ` on ${PLATFORM_LABEL[platform]}` : ""}`}
      >
        <Chips
          label="Period"
          items={PERIODS.map((p) => ({
            key: p,
            label: PERIOD_LABEL[p],
            href: hrefWith("/videos", sp, { period: p === "30d" ? null : p, page: null }),
            active: period === p,
          }))}
        />
      </PageHeader>

      <div className="mb-4 flex flex-col gap-2 lg:flex-row lg:items-center lg:justify-between">
        <Chips
          label="Platform"
          items={[
            {
              key: "all",
              label: "All platforms",
              href: hrefWith("/videos", sp, { platform: null, page: null }),
              active: !platform,
            },
            ...PLATFORMS.map((k) => ({
              key: k,
              label: (
                <>
                  <PlatformDot platform={k} /> {PLATFORM_LABEL[k]}
                </>
              ),
              href: hrefWith("/videos", sp, { platform: k, page: null }),
              active: platform === k,
            })),
          ]}
        />
        <div className="flex flex-wrap gap-2">
          {products.length > 1 && (
            <SelectNav
              label="Product"
              param="product"
              value={productId ?? ""}
              options={[{ value: "", label: "All products" }, ...products.map((p) => ({ value: p.id, label: p.name }))]}
            />
          )}
          <SelectNav
            label="Sort"
            param="sort"
            value={sort}
            options={POST_SORTS.map((s) => ({ value: s.id, label: `Sort: ${s.label}` }))}
          />
        </div>
      </div>

      <Card className="overflow-hidden">
        {rows.length === 0 && total > 0 ? (
          <Empty title="This page is past the end">
            <Link href={hrefWith("/videos", sp, { page: null })} className="text-accent-soft hover:text-accent-pale">
              Go to page 1 →
            </Link>
          </Empty>
        ) : rows.length === 0 ? (
          <Empty title={total === 0 && !platform ? "No videos yet" : "Nothing on this platform yet"}>
            {total === 0 && !platform ? "Videos appear here at the first check after they go live." : "Try another platform."}
          </Empty>
        ) : (
          <>
            {/* desktop table */}
            <div className="scroll-x hidden md:block">
              <table className="table">
                <thead>
                  <tr>
                    <th>Video</th>
                    <th className="r" title="Views gained in the selected period">
                      {periodCol}
                    </th>
                    <th className="r" title="Current view count">
                      Views
                    </th>
                    <th className="r" title="Views 24 hours after it went live (fair across videos of any age)">
                      24 h
                    </th>
                    <th className="r" title="Views 7 days after it went live">
                      7 d
                    </th>
                    <th className="r">Likes</th>
                    <th className="r">Comm.</th>
                    <th className="r">Shares</th>
                    <th className="r">Saves</th>
                    <th className="r" title="(likes + comments + shares + saves) / views">
                      Eng.
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {rows.map((r) => (
                    <tr key={r.id} className={r.active ? "" : "opacity-50"}>
                      <td className="max-w-[340px]">
                        <a href={r.url} target="_blank" rel="noreferrer" className="link-quiet flex items-center gap-1.5">
                          <span className="line-clamp-1">{r.caption || <span className="text-ink-faint">No caption</span>}</span>
                          <ExternalIcon />
                        </a>
                        <div className="mt-1 flex items-center gap-2 text-xs text-ink-faint">
                          <PlatformDot platform={r.platform} />
                          <span>{fmtHandle(r.platform, r.handle)}</span>
                          {showProduct && <span>· {r.productName}</span>}
                          <span title={fmtDateTime(r.postedAt ?? r.firstSeenAt)}>· {fmtAge(r.postedAt ?? r.firstSeenAt)}</span>
                          {!r.active && <span className="text-warn">· gone</span>}
                        </div>
                      </td>
                      <td className="r font-semibold">
                        <N v={r.periodViews} />
                      </td>
                      <td className="r">
                        <N v={r.views} />
                      </td>
                      <td className="r">
                        <N v={r.views24h} />
                      </td>
                      <td className="r">
                        <N v={r.views7d} />
                      </td>
                      <td className="r text-ink-dim">
                        <N v={r.likes} />
                      </td>
                      <td className="r text-ink-dim">
                        <N v={r.comments} />
                      </td>
                      <td className="r text-ink-dim">
                        <N v={r.shares} />
                      </td>
                      <td className="r text-ink-dim">
                        <N v={r.saves} />
                      </td>
                      <td className="r text-ink-dim">{pctFmt(r.engagement)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* phone cards */}
            <ul className="md:hidden">
              {rows.map((r) => (
                <li key={r.id} className={`border-t border-line px-4 py-3.5 first:border-t-0 ${r.active ? "" : "opacity-50"}`}>
                  <div className="flex items-center gap-2 text-xs text-ink-faint">
                    <PlatformDot platform={r.platform} />
                    <span>{fmtHandle(r.platform, r.handle)}</span>
                    {showProduct && <span>· {r.productName}</span>}
                    <span>· {fmtAge(r.postedAt ?? r.firstSeenAt)}</span>
                    {!r.active && <span className="text-warn">· gone</span>}
                  </div>
                  <a href={r.url} target="_blank" rel="noreferrer" className="link-quiet mt-1.5 line-clamp-2 block text-sm">
                    {r.caption || <span className="text-ink-faint">No caption</span>}
                  </a>
                  <div className="mt-2.5 grid grid-cols-4 gap-2 text-center">
                    {[
                      [periodCol, r.periodViews],
                      ["Views", r.views],
                      ["24 h", r.views24h],
                      ["7 d", r.views7d],
                    ].map(([label, v]) => (
                      <div key={label as string} className="rounded-lg bg-surface-2 px-1 py-1.5">
                        <p className="text-[10px] uppercase tracking-wider text-ink-faint">{label}</p>
                        <p className="text-sm font-semibold">
                          <N v={v as number | null} />
                        </p>
                      </div>
                    ))}
                  </div>
                  <p className="mt-2 text-xs text-ink-faint">
                    <N v={r.likes} /> likes · <N v={r.comments} /> comments · <N v={r.shares} /> shares · <N v={r.saves} /> saves
                    · {pctFmt(r.engagement)} eng.
                  </p>
                </li>
              ))}
            </ul>
          </>
        )}
      </Card>

      {pages > 1 && (
        <nav className="mt-4 flex items-center justify-between text-sm" aria-label="Pages">
          {page > 1 ? (
            <Link href={hrefWith("/videos", sp, { page: String(page - 1) })} className="btn-quiet rounded-lg px-3 py-2">
              ← Previous
            </Link>
          ) : (
            <span />
          )}
          <span className="text-ink-faint">
            Page {page} of {pages}
          </span>
          {page < pages ? (
            <Link href={hrefWith("/videos", sp, { page: String(page + 1) })} className="btn-quiet rounded-lg px-3 py-2">
              Next →
            </Link>
          ) : (
            <span />
          )}
        </nav>
      )}

      <p className="mt-6 text-xs leading-relaxed text-ink-faint">
        <strong className="font-medium text-ink-dim">24 h / 7 d</strong> = views a video had 24 hours / 7 days after it went live,
        read off its tracked curve: the fair way to compare a new video with an old one. Blank until the video is that old.
        Every row is one post on one platform: a video posted on Instagram, TikTok and Facebook is three rows.
        Instagram views are Instagram plays only (Facebook plays of a shared reel are not added). Facebook does not show saves.
      </p>
    </Shell>
  );
}
