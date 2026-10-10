import Link from "next/link";
import type { Metadata } from "next";
import Shell from "@/components/Shell";
import RunNowButton from "@/components/RunNowButton";
import { PlatformDot } from "@/components/platform";
import { Card, CardHead, PageHeader } from "@/components/ui";
import { poolLeftUsd } from "@/lib/apify/keys";
import { isPlatform, PLATFORM_LABEL } from "@/lib/config";
import { fmtDateTime, fmtUsd, timeAgo } from "@/lib/format";
import { runsPage } from "@/lib/queries";
import { requireSignIn } from "@/lib/session";

export const dynamic = "force-dynamic";
export const metadata: Metadata = { title: "Runs" };

const STATUS_STYLE: Record<string, string> = {
  ok: "border-accent/35 bg-accent/10 text-accent-pale",
  partial: "border-warn/35 bg-warn/10 text-warn",
  error: "border-bad/35 bg-bad/10 text-bad",
  budget_stop: "border-bad/35 bg-bad/10 text-bad",
  running: "border-accent/35 bg-accent/10 text-accent-soft",
};

const ACTOR_SHORT = (a: string | null) => (a ? (a.split("~")[1] ?? a) : "–");

const hh = (h: number) => `${String(h).padStart(2, "0")}:00`;

export default async function RunsPage() {
  await requireSignIn();
  const d = runsPage();
  const pct = d.budget > 0 ? Math.min(100, (d.monthSpend / d.budget) * 100) : 0;
  const alive = !!d.heartbeat && Date.now() - Date.parse(d.heartbeat) < 5 * 60_000;
  const initial = d.runningSince ? "running" : d.requestedAt ? "requested" : "idle";

  return (
    <Shell>
      <PageHeader title="Runs" sub="Every scraper run, what it cost, and whether the tracker is healthy">
        <RunNowButton initial={initial} />
      </PageHeader>

      <div className="mb-4 grid gap-4 md:grid-cols-3">
        <Card className="p-5">
          <p className="eyebrow">Health</p>
          <div className="mt-2 flex items-center gap-2">
            <span
              className="dot"
              style={{ background: d.health.ok ? "var(--color-accent)" : "var(--color-warn)", width: 10, height: 10 }}
            />
            <p className="text-lg font-semibold">{d.health.ok ? "All good" : "Needs attention"}</p>
          </div>
          {d.health.items.length > 0 ? (
            <ul className="mt-3 space-y-1.5 text-sm">
              {d.health.items.map((i, k) => (
                <li key={k} className={`flex gap-2 ${i.level === "alert" ? "text-warn" : "text-ink-dim"}`}>
                  <span aria-hidden="true">{i.level === "alert" ? "!" : "·"}</span>
                  <span>{i.text}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="mt-3 text-sm text-ink-dim">Scraper alive, recent runs succeeded, nothing unusual.</p>
          )}
        </Card>

        <Card className="p-5">
          <p className="eyebrow">Spend this month</p>
          <p className="num mt-2 text-2xl font-semibold tracking-tight">
            {fmtUsd(d.monthSpend)} <span className="text-sm font-normal text-ink-faint">of {fmtUsd(d.budget, 0)}</span>
          </p>
          <div className="bar-track mt-3">
            <div className="bar-fill" style={{ width: `${Math.max(pct, d.monthSpend > 0 ? 1.5 : 0)}%` }} />
          </div>
          <p className="mt-2 text-xs text-ink-dim">Last month {fmtUsd(d.lastMonthSpend)} · runs over the cap are skipped</p>
          {d.keyPool ? (
            <Link href="/keys" className="mt-3 block text-xs text-ink-dim transition-colors hover:text-ink">
              Apify keys: <span className="text-ink">{fmtUsd(poolLeftUsd(d.keyPool))}</span> left of{" "}
              {fmtUsd(d.keyPool.capUsd, 0)} · {d.keyPool.ok} of {d.keyPool.total} keys with credit ·{" "}
              <span className="text-accent-soft">see all keys →</span>
            </Link>
          ) : (
            <Link href="/keys" className="mt-3 block text-xs text-ink-faint hover:text-ink">
              Apify keys not checked yet →
            </Link>
          )}
        </Card>

        <Card className="p-5">
          <p className="eyebrow">Scraper</p>
          <div className="mt-2 flex items-center gap-2">
            <span
              className={`dot ${d.runningSince ? "pulse-dot" : ""}`}
              style={{ background: alive ? "var(--color-accent)" : "var(--color-warn)", width: 10, height: 10 }}
            />
            <p className="text-lg font-semibold">
              {d.runningSince ? "Scraping now" : alive ? "Waiting for the next slot" : "Not running"}
            </p>
          </div>
          <dl className="mt-3 grid grid-cols-[auto_1fr] gap-x-3 gap-y-1.5 text-xs">
            <dt className="text-ink-faint">Last cycle</dt>
            <dd className="text-ink-dim">
              {d.lastCycle ? `${timeAgo(d.lastCycle.at)} (${d.lastCycle.trigger}, ${d.lastCycle.seconds} s)` : "none yet"}
            </dd>
            <dt className="text-ink-faint">New posts</dt>
            <dd className="text-ink-dim">checked at {d.schedule.discovery.map(hh).join(", ")}</dd>
            <dt className="text-ink-faint">Followers</dt>
            <dd className="text-ink-dim">daily at {d.schedule.profiles.map(hh).join(", ")} (TikTok with every check)</dd>
            <dt className="text-ink-faint">Older posts</dt>
            <dd className="text-ink-dim">re-checked at {hh(d.schedule.anchor)}, by age</dd>
            <dt className="text-ink-faint">Tracked</dt>
            <dd className="text-ink-dim">
              {d.postsTracked} posts · {d.snapshots} snapshots
            </dd>
          </dl>
          <p className="mt-2 text-[11px] text-ink-faint">Times are {d.schedule.timezone} time.</p>
        </Card>
      </div>

      <Card className="overflow-hidden">
        <CardHead
          title="Recent runs"
          sub="One row per scraper run (newest first). Cost is Apify's own figure, final ~10 min after a run."
        />
        {d.runs.length === 0 ? (
          <p className="px-5 py-8 text-sm text-ink-dim">No runs yet. The scraper starts its first cycle as soon as it is up.</p>
        ) : (
          <>
            <ul className="mt-3 border-t border-line md:hidden">
              {d.runs.map((r) => (
                <li key={r.id} className="border-t border-line px-4 py-3 first:border-t-0">
                  <div className="flex items-center gap-2 text-sm">
                    {isPlatform(r.platform) && <PlatformDot platform={r.platform} />}
                    <span>{r.kind}</span>
                    <span className="text-ink-faint">{isPlatform(r.platform) ? PLATFORM_LABEL[r.platform] : ""}</span>
                    {r.trigger_source === "manual" && <span className="text-xs text-accent-soft">manual</span>}
                    <span
                      className={`ml-auto rounded-md border px-1.5 py-0.5 text-[11px] font-medium ${STATUS_STYLE[r.status] ?? "border-line text-ink-dim"}`}
                    >
                      {r.status.replace("_", " ")}
                    </span>
                  </div>
                  <p className="mt-1 text-xs text-ink-faint">
                    {fmtDateTime(r.started_at)} · {r.items_ok} ok{r.items_failed ? ` · ${r.items_failed} failed` : ""} ·{" "}
                    {r.cost_usd ? `$${r.cost_usd.toFixed(3)}` : "$0"} · {ACTOR_SHORT(r.actor)}
                  </p>
                  {r.error && <p className="mt-1 text-xs text-ink-dim">{r.error}</p>}
                </li>
              ))}
            </ul>
            <div className="scroll-x mt-3 hidden border-t border-line md:block">
              <table className="table min-w-[820px]">
                <thead>
                  <tr>
                    <th>When</th>
                    <th>What</th>
                    <th>Scraper</th>
                    <th>Status</th>
                    <th className="r">OK</th>
                    <th className="r">Failed</th>
                    <th className="r">Cost</th>
                    <th>Note</th>
                  </tr>
                </thead>
                <tbody>
                  {d.runs.map((r) => {
                    const secs = r.finished_at ? Math.round((Date.parse(r.finished_at) - Date.parse(r.started_at)) / 1000) : null;
                    return (
                      <tr key={r.id}>
                        <td className="whitespace-nowrap text-ink-dim" title={r.started_at}>
                          {fmtDateTime(r.started_at)}
                          {secs !== null && <span className="ml-1.5 text-xs text-ink-faint">{secs}s</span>}
                        </td>
                        <td className="whitespace-nowrap">
                          <span className="inline-flex items-center gap-1.5">
                            {isPlatform(r.platform) && <PlatformDot platform={r.platform} />}
                            <span>{r.kind}</span>
                            <span className="text-ink-faint">{isPlatform(r.platform) ? PLATFORM_LABEL[r.platform] : ""}</span>
                            {r.trigger_source === "manual" && <span className="text-xs text-accent-soft">manual</span>}
                          </span>
                        </td>
                        <td className="whitespace-nowrap font-mono text-xs text-ink-faint" title={r.actor ?? ""}>
                          {ACTOR_SHORT(r.actor)}
                        </td>
                        <td>
                          <span
                            className={`rounded-md border px-1.5 py-0.5 text-[11px] font-medium ${STATUS_STYLE[r.status] ?? "border-line text-ink-dim"}`}
                          >
                            {r.status.replace("_", " ")}
                          </span>
                        </td>
                        <td className="r">{r.items_ok}</td>
                        <td className={`r ${r.items_failed ? "text-warn" : "text-ink-faint"}`}>{r.items_failed}</td>
                        <td className="r text-ink-dim" title={r.cost_final ? "final" : "provisional"}>
                          {r.cost_usd ? `$${r.cost_usd.toFixed(3)}` : "–"}
                          {!r.cost_final && r.cost_usd > 0 && <span className="text-ink-faint">*</span>}
                        </td>
                        <td className="max-w-[320px] text-xs text-ink-faint">
                          <span className="line-clamp-2">{r.error ?? ""}</span>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </>
        )}
      </Card>
    </Shell>
  );
}
