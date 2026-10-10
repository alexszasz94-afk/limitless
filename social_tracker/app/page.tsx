import type { ReactNode } from "react";
import Link from "next/link";
import Shell from "@/components/Shell";
import DailyChart from "@/components/DailyChart";
import Avatar from "@/components/Avatar";
import { PlatformDot, PlatformTag } from "@/components/platform";
import { Card, CardHead, Change, Chips, Empty, ExternalIcon, N, PageHeader } from "@/components/ui";
import { PLATFORMS, PLATFORM_LABEL, loadCadence } from "@/lib/config";
import { getDb } from "@/lib/db";
import { fmtAge, fmtFull, fmtHandle, fmtSigned, pctChange, timeAgo } from "@/lib/format";
import { PERIODS, PERIOD_LABEL, type TopPost, listProducts, overview, parsePeriod, parseProduct } from "@/lib/queries";
import { requireSignIn } from "@/lib/session";
import { flatParams, hrefWith } from "@/lib/url";

export const dynamic = "force-dynamic";

export default async function OverviewPage({
  searchParams,
}: {
  searchParams: Promise<Record<string, string | string[] | undefined>>;
}) {
  await requireSignIn();
  const sp = flatParams(await searchParams);
  const db = getDb();
  const productId = parseProduct(db, sp.product);
  const period = parsePeriod(sp.period);
  const data = overview(productId, period);
  const products = listProducts(db).filter((p) => p.active || p.id === productId);
  const t = data.totals;
  const periodLabel = PERIOD_LABEL[period].toLowerCase();
  const scopeName = productId ? products.find((p) => p.id === productId)?.name : "All products";
  const platformTotals = PLATFORMS.map((k) => ({ k, v: data.series.reduce((s, d) => s + d.values[k], 0) }));
  const cadence = loadCadence();
  const noPosts = t.posts === 0;
  const showProduct = !productId && products.length > 1;

  return (
    <Shell>
      <PageHeader
        title="Overview"
        sub={
          <>
            {scopeName} · {period === "all" ? "all time" : `last ${periodLabel}`}
          </>
        }
      >
        <div className="flex flex-col gap-2 sm:items-end">
          {products.length > 1 && (
            <Chips
              label="Product"
              items={[
                { key: "all", label: "All products", href: hrefWith("/", sp, { product: null }), active: !productId },
                ...products.map((p) => ({
                  key: p.id,
                  label: p.name,
                  href: hrefWith("/", sp, { product: p.id }),
                  active: productId === p.id,
                })),
              ]}
            />
          )}
          <Chips
            label="Period"
            items={PERIODS.map((p) => ({
              key: p,
              label: PERIOD_LABEL[p],
              href: hrefWith("/", sp, { period: p === "30d" ? null : p }),
              active: period === p,
            }))}
          />
        </div>
      </PageHeader>

      {/* hero */}
      <Card className="relative mb-4 overflow-hidden p-5 sm:p-6">
        <div
          className="pointer-events-none absolute -right-24 -top-28 h-72 w-72 rounded-full"
          style={{ background: "radial-gradient(circle, rgba(77,141,255,0.22), transparent 65%)" }}
          aria-hidden="true"
        />
        <div className="relative grid gap-6 lg:grid-cols-[1.35fr_2fr] lg:items-end">
          <div>
            <p className="eyebrow">Total views</p>
            <p className="hero-number mt-2 text-5xl font-semibold sm:text-6xl" title={fmtFull(t.totalViews)}>
              {fmtFull(t.totalViews)}
            </p>
            <p className="mt-2 text-sm text-ink-dim">
              Every tracked video&apos;s current count, summed · {t.posts} video{t.posts === 1 ? "" : "s"} on {t.accounts} account
              {t.accounts === 1 ? "" : "s"}
            </p>
          </div>
          <div className="grid grid-cols-2 gap-x-5 gap-y-5 sm:grid-cols-4">
            <div>
              <p className="eyebrow">Gained, {period === "all" ? "all time" : periodLabel}</p>
              <p className="num mt-1.5 text-2xl font-semibold tracking-tight">
                <N v={data.totals.periodViews} />
              </p>
              <div className="mt-1">
                {t.prevPeriodViews ? (
                  <Change
                    value={pctChange(t.periodViews, t.prevPeriodViews)}
                    suffix={`vs previous ${period === "all" ? "" : periodLabel}`}
                  />
                ) : (
                  <span className="text-xs text-ink-faint">
                    {period === "all" ? "since tracking began" : "nothing to compare yet"}
                  </span>
                )}
              </div>
            </div>
            <div>
              <p className="eyebrow">Today</p>
              <p className="num mt-1.5 text-2xl font-semibold tracking-tight">
                <N v={t.today} />
              </p>
              <p className="mt-1 text-xs text-ink-dim">
                Yesterday <N v={t.yesterday} className="text-ink" />
              </p>
            </div>
            <div>
              <p className="eyebrow">Followers</p>
              <p className="num mt-1.5 text-2xl font-semibold tracking-tight">
                <N v={t.followers} />
              </p>
              <p className="mt-1 text-xs text-ink-dim">
                {t.followersChange === null
                  ? "–"
                  : `${fmtSigned(t.followersChange)} ${t.followersSinceStart || period === "all" ? "since tracking began" : `in ${periodLabel}`}`}
              </p>
            </div>
            <div>
              <p className="eyebrow">New videos</p>
              <p className="num mt-1.5 text-2xl font-semibold tracking-tight">{t.postsInPeriod}</p>
              <p className="mt-1 text-xs text-ink-dim">{period === "all" ? "all time" : `in ${periodLabel}`}</p>
            </div>
          </div>
        </div>
      </Card>

      {/* chart */}
      <Card className="mb-4 pb-4">
        <CardHead
          title="Views gained per day"
          sub="New views each day (local time), from the day-by-day difference of every video's count"
          aside={
            <div className="hidden flex-wrap justify-end gap-x-4 gap-y-1 sm:flex">
              {platformTotals.map(({ k, v }) => (
                <span key={k} className="flex items-center gap-1.5 text-xs text-ink-dim">
                  <PlatformDot platform={k} />
                  {PLATFORM_LABEL[k]} <N v={v} className="text-ink" />
                </span>
              ))}
            </div>
          }
        />
        <div className="mt-2 flex flex-wrap gap-x-4 gap-y-1 px-5 sm:hidden">
          {platformTotals.map(({ k, v }) => (
            <span key={k} className="flex items-center gap-1.5 text-xs text-ink-dim">
              <PlatformDot platform={k} />
              {PLATFORM_LABEL[k]} <N v={v} className="text-ink" />
            </span>
          ))}
        </div>
        <div className="mt-3 px-3 sm:px-4">
          <DailyChart points={data.series} />
        </div>
      </Card>

      {/* products */}
      {data.products.map((p) => (
        <Card key={p.id} className="mb-4 overflow-hidden">
          <div className="flex flex-col gap-4 px-5 pb-4 pt-5 sm:flex-row sm:items-center sm:justify-between">
            <div className="flex min-w-0 items-center gap-3">
              <Avatar src={p.avatar} name={p.name} size={44} />
              <div className="min-w-0">
                <h2 className="truncate text-lg font-semibold tracking-tight">{p.name}</h2>
                <p className="text-xs text-ink-faint">
                  {p.accounts.length} account{p.accounts.length === 1 ? "" : "s"} · {p.posts} video{p.posts === 1 ? "" : "s"}{" "}
                  tracked
                </p>
              </div>
            </div>
            <div className="grid grid-cols-3 gap-5 sm:flex sm:gap-8">
              <div>
                <p className="eyebrow">Total</p>
                <p className="mt-1 text-lg font-semibold">
                  <N v={p.totalViews} />
                </p>
              </div>
              <div>
                <p className="eyebrow">{period === "all" ? "Gained" : PERIOD_LABEL[period]}</p>
                <p className="mt-1 text-lg font-semibold">
                  <N v={p.periodViews} />
                </p>
              </div>
              <div>
                <p className="eyebrow">Followers</p>
                <p className="mt-1 text-lg font-semibold">
                  <N v={p.followers} />
                </p>
              </div>
            </div>
          </div>
          <ul className="border-t border-line md:hidden">
            {p.accounts.map((a) => (
              <li key={a.id} className={`border-t border-line px-4 py-3 first:border-t-0 ${a.active ? "" : "opacity-50"}`}>
                <a
                  href={a.url}
                  target="_blank"
                  rel="noreferrer"
                  className="link-quiet flex items-center gap-2 text-sm font-medium"
                >
                  <PlatformDot platform={a.platform} />
                  <span className="text-ink-dim">{PLATFORM_LABEL[a.platform]}</span>
                  <span className="truncate">{fmtHandle(a.platform, a.handle)}</span>
                  <ExternalIcon />
                  <span className="ml-auto shrink-0 text-xs font-normal text-ink-faint">
                    {a.active ? timeAgo(a.lastChecked) : "paused"}
                  </span>
                </a>
                <div className="mt-2 grid grid-cols-4 gap-2 text-center">
                  {(
                    [
                      ["Followers", a.followers],
                      ["Videos", a.posts],
                      [period === "all" ? "Gained" : PERIOD_LABEL[period], a.periodViews],
                      ["Total", a.totalViews],
                    ] as Array<[string, number | null]>
                  ).map(([label, v]) => (
                    <div key={label} className="rounded-lg bg-surface-2 px-1 py-1.5">
                      <p className="text-[10px] uppercase tracking-wider text-ink-faint">{label}</p>
                      <p className="text-sm font-semibold">
                        <N v={v} />
                      </p>
                    </div>
                  ))}
                </div>
                {a.followersChange !== null && a.followersChange !== 0 && (
                  <p className={`mt-1.5 text-xs ${a.followersChange > 0 ? "text-good" : "text-bad"}`}>
                    {fmtSigned(a.followersChange)} followers{" "}
                    {a.followersSinceStart || period === "all" ? "since tracking began" : `in ${periodLabel}`}
                  </p>
                )}
              </li>
            ))}
          </ul>
          <div className="scroll-x hidden border-t border-line md:block">
            <table className="table min-w-[640px]">
              <thead>
                <tr>
                  <th>Account</th>
                  <th className="r">Followers</th>
                  <th className="r">Videos</th>
                  <th className="r">{period === "all" ? "Gained" : PERIOD_LABEL[period]}</th>
                  <th className="r">Total views</th>
                  <th className="r">Checked</th>
                </tr>
              </thead>
              <tbody>
                {p.accounts.map((a) => (
                  <tr key={a.id} className={a.active ? "" : "opacity-50"}>
                    <td>
                      <a
                        href={a.url}
                        target="_blank"
                        rel="noreferrer"
                        className="link-quiet inline-flex items-center gap-2 font-medium"
                      >
                        <PlatformDot platform={a.platform} />
                        <span className="text-ink-dim">{PLATFORM_LABEL[a.platform]}</span>
                        <span>{fmtHandle(a.platform, a.handle)}</span>
                        <ExternalIcon />
                      </a>
                      {!a.active && <span className="ml-2 text-xs text-ink-faint">paused</span>}
                    </td>
                    <td className="r">
                      <N v={a.followers} />
                      {a.followersChange !== null && a.followersChange !== 0 && (
                        <span className={`ml-1.5 text-xs ${a.followersChange > 0 ? "text-good" : "text-bad"}`}>
                          {fmtSigned(a.followersChange)}
                        </span>
                      )}
                    </td>
                    <td className="r">{a.posts}</td>
                    <td className="r">
                      <N v={a.periodViews} />
                    </td>
                    <td className="r">
                      <N v={a.totalViews} />
                    </td>
                    <td className="r text-xs text-ink-faint">{timeAgo(a.lastChecked)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Card>
      ))}

      {noPosts ? (
        <Card>
          <Empty title="No videos yet">
            The accounts are checked {cadence.discovery.atHours.length} times a day (
            {cadence.discovery.atHours.map((h) => `${String(h).padStart(2, "0")}:00`).join(", ")}). New reels show up here at the
            next check after they go live, and their views are followed from then on.
          </Empty>
        </Card>
      ) : (
        <div className="grid gap-4 lg:grid-cols-2">
          <Ranking
            title="Top videos"
            sub={`Most views gained in ${period === "all" ? "total" : `the last ${periodLabel}`}`}
            href={hrefWith("/videos", sp, { sort: null })}
            rows={data.topPosts}
            showProduct={showProduct}
            main={(p) => p.periodViews}
            second={(p) => (
              <>
                <N v={p.views} /> total
              </>
            )}
          />
          <Ranking
            title="Best first 24 hours"
            sub={`Views 24 h after going live · videos posted ${period === "all" ? "any time" : `in the last ${periodLabel}`}`}
            href={hrefWith("/videos", sp, { sort: "v24" })}
            rows={data.bestStarts}
            empty={`No video${period === "all" ? "" : ` posted in the last ${periodLabel}`} has a 24-hour count yet. A video shows here once it has been tracked through its first day.`}
            showProduct={showProduct}
            main={(p) => p.views24h}
            second={(p) => (
              <>
                <N v={p.views} /> now
              </>
            )}
          />
        </div>
      )}
    </Shell>
  );
}

/** A top-5 list of videos (each one post on one platform), linking to the platform. */
function Ranking({
  title,
  sub,
  href,
  rows,
  empty,
  showProduct,
  main,
  second,
}: {
  title: string;
  sub: string;
  href: string;
  rows: TopPost[];
  empty?: string;
  showProduct: boolean;
  main: (p: TopPost) => number | null;
  second: (p: TopPost) => ReactNode;
}) {
  return (
    <Card className="pb-2">
      <CardHead
        title={title}
        sub={sub}
        aside={
          <Link href={href} className="shrink-0 text-xs font-medium text-accent-soft hover:text-accent-pale">
            All videos →
          </Link>
        }
      />
      {rows.length === 0 ? (
        <p className="px-5 py-6 text-sm text-ink-dim">{empty ?? "Nothing in this period yet."}</p>
      ) : (
        <ol className="mt-2">
          {rows.map((p, i) => (
            <li key={p.id} className="flex items-center gap-3 border-t border-line px-5 py-3 first:border-t-0">
              <span className="num w-4 shrink-0 text-xs text-ink-faint">{i + 1}</span>
              <div className="min-w-0 flex-1">
                <a href={p.url} target="_blank" rel="noreferrer" className="link-quiet flex items-center gap-1.5 text-sm">
                  <span className="line-clamp-1">{p.caption || <span className="text-ink-faint">No caption</span>}</span>
                  <ExternalIcon />
                </a>
                <div className="mt-1 flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-ink-faint">
                  <PlatformTag platform={p.platform} />
                  {showProduct && <span>{p.productName}</span>}
                  <span>{fmtAge(p.postedAt)} old</span>
                </div>
              </div>
              <div className="shrink-0 text-right">
                <p className="text-sm font-semibold">
                  <N v={main(p)} />
                </p>
                <p className="text-xs text-ink-faint">{second(p)}</p>
              </div>
            </li>
          ))}
        </ol>
      )}
    </Card>
  );
}
