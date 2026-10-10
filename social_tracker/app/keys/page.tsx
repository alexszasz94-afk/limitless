import type { Metadata } from "next";
import Shell from "@/components/Shell";
import CheckKeysButton from "@/components/CheckKeysButton";
import { Card, CardHead, Chips, Empty, PageHeader } from "@/components/ui";
import { fmtDateTime, fmtUsd, timeAgo } from "@/lib/format";
import { poolLeftUsd } from "@/lib/apify/keys";
import { keysPage } from "@/lib/queries";
import { requireSignIn } from "@/lib/session";
import { flatParams, hrefWith } from "@/lib/url";

export const dynamic = "force-dynamic";
export const metadata: Metadata = { title: "Apify keys" };

const SHOW = [
  { id: "all", label: "All" },
  { id: "ok", label: "With credit" },
  { id: "used up", label: "Used up" },
  { id: "invalid", label: "Invalid" },
  { id: "not reached", label: "Not reached" },
] as const;

const STATUS_STYLE: Record<string, string> = {
  ok: "border-accent/35 bg-accent/10 text-accent-pale",
  "used up": "border-warn/35 bg-warn/10 text-warn",
  invalid: "border-bad/35 bg-bad/10 text-bad",
  "not reached": "border-line bg-white/5 text-ink-dim",
};

/** "10 Oct" from YYYY-MM-DD (UTC date of the reset). */
function shortDate(d: string): string {
  const [y, m, day] = d.split("-").map(Number);
  return new Intl.DateTimeFormat("en-GB", { timeZone: "UTC", day: "numeric", month: "short" }).format(
    new Date(Date.UTC(y, m - 1, day)),
  );
}

function resetDate(cycleEnd: string | null): string {
  if (!cycleEnd) return "–";
  return shortDate(new Date(Date.parse(cycleEnd) + 1).toISOString().slice(0, 10));
}

function Bar({ used, cap }: { used: number; cap: number }) {
  const pct = cap > 0 ? Math.min(100, (used / cap) * 100) : 0;
  return (
    <div className="bar-track" aria-hidden="true">
      <div className="bar-fill" style={{ width: `${pct}%` }} />
    </div>
  );
}

export default async function KeysPage({
  searchParams,
}: {
  searchParams: Promise<Record<string, string | string[] | undefined>>;
}) {
  await requireSignIn();
  const sp = flatParams(await searchParams);
  const show = SHOW.some((s) => s.id === sp.show) ? (sp.show as (typeof SHOW)[number]["id"]) : "all";
  const d = keysPage();
  const s = d.summary;
  const left = s ? poolLeftUsd(s) : 0;
  const rows = d.keys.filter((k) => show === "all" || k.status === show);

  return (
    <Shell>
      <PageHeader
        title="Apify keys"
        sub={
          s
            ? `All ${s.total} Apify keys - checked ${timeAgo(s.checkedAt)}, and automatically every hour`
            : "Not checked yet - press Check now"
        }
      >
        <CheckKeysButton />
      </PageHeader>

      {!s ? (
        <Card>
          <Empty title="No key check yet">The scraper checks every key once an hour; Check now does it straight away.</Empty>
        </Card>
      ) : (
        <>
          <div className="mb-4 grid gap-4 md:grid-cols-2 lg:grid-cols-4">
            <Card className="p-5">
              <p className="eyebrow">Credit left</p>
              <p className="num mt-2 text-3xl font-semibold tracking-tight">{fmtUsd(left)}</p>
              <p className="mt-1 text-xs text-ink-dim">of {fmtUsd(s.capUsd, 0)} across all keys this cycle · the bar is what is spent</p>
              <div className="mt-3">
                <Bar used={s.usedUsd} cap={s.capUsd} />
              </div>
            </Card>
            <Card className="p-5">
              <p className="eyebrow">Spent this cycle</p>
              <p className="num mt-2 text-3xl font-semibold tracking-tight">{fmtUsd(s.usedUsd)}</p>
              <p className="mt-1 text-xs leading-relaxed text-ink-dim">
                Everything the keys ran: this tracker and anything else you use them for. This tracker alone:{" "}
                <span className="text-ink">{fmtUsd(d.trackerMonthSpend)}</span> this month.
              </p>
            </Card>
            <Card className="p-5">
              <p className="eyebrow">Keys</p>
              <p className="num mt-2 text-3xl font-semibold tracking-tight">
                {s.ok} <span className="text-base font-normal text-ink-faint">of {s.total} with credit</span>
              </p>
              <p className="mt-1 text-xs text-ink-dim">
                {s.overCap} used up · {s.invalid} invalid
                {s.notReached ? ` · ${s.notReached} not reached (network - check again)` : ""}
                {s.runningNow ? ` · ${s.runningNow} run${s.runningNow === 1 ? "" : "s"} going now` : ""}
              </p>
            </Card>
            <Card className="p-5">
              <p className="eyebrow">Next resets</p>
              {d.resets.length === 0 ? (
                <p className="mt-2 text-sm text-ink-dim">–</p>
              ) : (
                <ul className="mt-2 space-y-1.5 text-sm">
                  {d.resets.slice(0, 4).map((r) => (
                    <li key={r.date} className="flex items-baseline justify-between gap-3">
                      <span className="text-ink-dim">
                        {shortDate(r.date)}{" "}
                        <span className="text-xs text-ink-faint">
                          · {r.keys} key{r.keys === 1 ? "" : "s"}
                        </span>
                      </span>
                      <span className="num font-medium text-accent-pale">+{fmtUsd(r.freedUsd)}</span>
                    </li>
                  ))}
                </ul>
              )}
              <p className="mt-2 text-[11px] text-ink-faint">Each key resets on its own day (UTC).</p>
            </Card>
          </div>

          <Card className="overflow-hidden">
            <CardHead
              title="Every key"
              sub="Numbered in APIFY_TOKENS order (#1 = the first key); only the last characters are shown"
            />
            <div className="mt-3 px-5">
              <Chips
                label="Show"
                items={SHOW.filter((o) => o.id !== "not reached" || d.keys.some((k) => k.status === o.id)).map((o) => ({
                  key: o.id,
                  label: `${o.label} ${o.id === "all" ? d.keys.length : d.keys.filter((k) => k.status === o.id).length}`,
                  href: hrefWith("/keys", sp, { show: o.id === "all" ? null : o.id }),
                  active: show === o.id,
                }))}
              />
            </div>

            {/* desktop */}
            <div className="scroll-x mt-3 hidden border-t border-line md:block">
              <table className="table">
                <thead>
                  <tr>
                    <th className="r">#</th>
                    <th>Key</th>
                    <th>Status</th>
                    <th className="r">Spent</th>
                    <th className="r">Cap</th>
                    <th className="r">Left</th>
                    <th className="w-40"></th>
                    <th>Resets</th>
                    <th className="r">Running</th>
                  </tr>
                </thead>
                <tbody>
                  {rows.map((k) => (
                    <tr key={k.n}>
                      <td className="r text-ink-faint">{k.n}</td>
                      <td className="font-mono text-xs text-ink-dim">{k.label}</td>
                      <td>
                        <span className={`rounded-md border px-1.5 py-0.5 text-[11px] font-medium ${STATUS_STYLE[k.status]}`}>
                          {k.status}
                        </span>
                      </td>
                      <td className="r">{k.usedUsd === null ? "–" : fmtUsd(k.usedUsd)}</td>
                      <td className="r text-ink-dim">{k.capUsd === null ? "–" : fmtUsd(k.capUsd, 0)}</td>
                      <td className="r font-medium">
                        {k.capUsd === null || k.usedUsd === null ? "–" : fmtUsd(Math.max(0, k.capUsd - k.usedUsd))}
                      </td>
                      <td>{k.capUsd !== null && k.usedUsd !== null && <Bar used={k.usedUsd} cap={k.capUsd} />}</td>
                      <td
                        className="whitespace-nowrap text-ink-dim"
                        title={k.cycleEnd ? `cycle ends ${fmtDateTime(k.cycleEnd)}` : undefined}
                      >
                        {resetDate(k.cycleEnd)}
                      </td>
                      <td className="r text-ink-dim">{k.runningNow || ""}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* phone */}
            <ul className="mt-3 border-t border-line md:hidden">
              {rows.map((k) => (
                <li key={k.n} className="border-t border-line px-4 py-3 first:border-t-0">
                  <div className="flex items-center gap-2 text-sm">
                    <span className="num w-8 text-xs text-ink-faint">#{k.n}</span>
                    <span className="font-mono text-xs text-ink-dim">{k.label}</span>
                    <span className={`ml-auto rounded-md border px-1.5 py-0.5 text-[11px] font-medium ${STATUS_STYLE[k.status]}`}>
                      {k.status}
                    </span>
                  </div>
                  {k.capUsd !== null && k.usedUsd !== null && (
                    <>
                      <div className="mt-2">
                        <Bar used={k.usedUsd} cap={k.capUsd} />
                      </div>
                      <p className="mt-1.5 text-xs text-ink-faint">
                        {fmtUsd(Math.max(0, k.capUsd - k.usedUsd))} left of {fmtUsd(k.capUsd, 0)} · resets {resetDate(k.cycleEnd)}
                        {k.runningNow ? ` · ${k.runningNow} running` : ""}
                      </p>
                    </>
                  )}
                </li>
              ))}
            </ul>
            {rows.length === 0 && <p className="px-5 py-6 text-sm text-ink-dim">No keys in this group.</p>}
          </Card>
        </>
      )}
    </Shell>
  );
}
