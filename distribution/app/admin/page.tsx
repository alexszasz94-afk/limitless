import type { Metadata } from "next";
import { cookies, headers } from "next/headers";
import { redirect } from "next/navigation";
import { isAdminSession, adminCookieName, adminCookieValue, adminConfigured } from "@/lib/admin";
import {
  getAllPosters,
  getPersona,
  getCompletedCountByDay,
  countQueued,
  countPosted,
  lastActivity,
} from "@/lib/db";
import { dayPosition, dayTasks, elapsedDays, CONTENT_TASK_KIND } from "@/lib/day";
import { tasksForDay } from "@/lib/config";
import Mark from "@/components/Mark";
import { CopyButton } from "@/components/ui";

export const dynamic = "force-dynamic";
export const metadata: Metadata = { title: "Admin" };

async function login(formData: FormData) {
  "use server";
  // Secure cookie only over HTTPS, so logging in also works over plain http (LAN, first deploy).
  const https = (await headers()).get("x-forwarded-proto") === "https";
  const value = adminCookieValue(String(formData.get("passphrase") ?? ""));
  if (!value) {
    await new Promise((r) => setTimeout(r, 800)); // slow down guessing
    redirect("/admin?e=1");
  }
  (await cookies()).set(adminCookieName(), value, {
    httpOnly: true,
    sameSite: "lax",
    secure: https,
    maxAge: 60 * 60 * 24 * 30,
    path: "/",
  });
  redirect("/admin");
}

async function logout() {
  "use server";
  (await cookies()).delete(adminCookieName());
  redirect("/admin");
}

const KIND_ORDER = ["reel", "story", "highlight_cover"];
const KIND_LABEL: Record<string, string> = { reel: "reels", story: "stories", highlight_cover: "highlight covers" };

function timeAgo(iso: string | null): string {
  if (!iso) return "never";
  const s = Math.max(0, (Date.now() - Date.parse(iso)) / 1000);
  if (s < 90) return "just now";
  if (s < 3600) return `${Math.round(s / 60)} min ago`;
  if (s < 86400) return `${Math.round(s / 3600)} h ago`;
  return `${Math.round(s / 86400)} d ago`;
}

/** How many items of each kind the next `days` days will draw from the queue
 *  (from the day after the current one: today's items are already handed out). */
function upcomingNeed(day: number, personaId: string, days: number): Record<string, number> {
  const need: Record<string, number> = {};
  for (let d = day + 1; d <= day + days; d++) {
    for (const t of tasksForDay(d, personaId)) {
      const kind = CONTENT_TASK_KIND[t.type];
      if (kind) need[kind] = (need[kind] ?? 0) + 1;
    }
  }
  return need;
}

export default async function AdminPage({
  searchParams,
}: {
  searchParams: Promise<{ e?: string }>;
}) {
  const { e } = await searchParams;
  const authed = isAdminSession(await cookies());

  if (!authed) {
    return (
      <main className="mx-auto flex min-h-dvh max-w-sm flex-col justify-center px-6">
        <div className="mb-8 flex items-center gap-3">
          <Mark size={44} />
          <div>
            <p className="eyebrow">Distribution</p>
            <h1 className="text-2xl font-semibold tracking-tight">Admin</h1>
          </div>
        </div>
        <form action={login} className="flex flex-col gap-3">
          <input
            type="password"
            name="passphrase"
            placeholder="Passphrase"
            autoComplete="current-password"
            autoFocus
            required
            className="rounded-xl border border-line bg-surface px-4 py-3.5 text-base text-ink outline-none transition-colors placeholder:text-ink-faint focus:border-accent"
          />
          <button type="submit" className="btn-primary rounded-xl py-3.5">
            Enter
          </button>
        </form>
        {e && <p className="mt-4 text-sm text-warn">Wrong passphrase.</p>}
        {!adminConfigured() && (
          <p className="mt-4 text-sm text-ink-faint">
            ADMIN_PASSPHRASE is not set (or still &quot;change-me&quot;). Set it in .env and restart.
          </p>
        )}
      </main>
    );
  }

  const h = await headers();
  const host = h.get("x-forwarded-host") ?? h.get("host") ?? "localhost:3000";
  const proto = h.get("x-forwarded-proto") ?? "http";
  const origin = `${proto}://${host}`;

  const rows = getAllPosters().map((p) => {
    const persona = getPersona(p.persona_id);
    const { day, waitForTomorrow } = dayPosition(p);
    const elapsed = elapsedDays(p);
    const tasks = dayTasks(p, day).length;
    const done = getCompletedCountByDay(p.id).get(day) ?? 0;
    const drift = elapsed - (day - 1);
    const queues = countQueued(p.persona_id);
    const need = upcomingNeed(day, p.persona_id, 3);
    const low = Object.entries(need).filter(([k, n]) => (queues[k] ?? 0) < n).map(([k]) => k);
    // Show the queues this persona uses: anything still queued, anything the next days need, reels always.
    const kinds = KIND_ORDER.filter((k) => k === "reel" || (queues[k] ?? 0) > 0 || need[k]);
    return { p, persona, day, waitForTomorrow, elapsed, tasks, done, drift, queues, kinds, low, posted: countPosted(p.id), last: lastActivity(p.id) };
  });

  const drifting = rows.filter((r) => r.drift > 1).length;
  const totalPosted = rows.reduce((s, r) => s + r.posted, 0);
  const lowQueues = rows.filter((r) => r.low.length).length;

  return (
    <main className="mx-auto max-w-3xl px-5 pb-16 pt-10">
      <header className="mb-8 flex items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <Mark size={40} />
          <div>
            <p className="eyebrow">Distribution</p>
            <h1 className="text-2xl font-semibold tracking-tight">Posters</h1>
          </div>
        </div>
        <form action={logout}>
          <button type="submit" className="btn-quiet rounded-lg px-3 py-2 text-sm text-ink-dim">
            Log out
          </button>
        </form>
      </header>

      <div className="mb-8 grid grid-cols-2 gap-3 sm:grid-cols-4">
        <Stat label="Posters" value={rows.length} />
        <Stat label="Videos posted" value={totalPosted} />
        <Stat label="Drifting" value={drifting} warn={drifting > 0} />
        <Stat label="Queues low" value={lowQueues} warn={lowQueues > 0} />
      </div>

      <p className="mb-4 text-sm text-ink-dim">
        Personal day vs. calendar days since start. Drift means missed days (the schedule slips, content is never
        skipped); ahead means several days done in one sitting.
      </p>

      <div className="flex flex-col gap-3">
        {rows.map((r) => {
          const url = `${origin}/d/${r.p.token}`;
          const pct = r.tasks ? Math.round((r.done / r.tasks) * 100) : 0;
          return (
            <div key={r.p.id} className="card rounded-2xl p-5">
              <div className="flex items-start justify-between gap-4">
                <div className="min-w-0">
                  <div className="font-semibold">{r.p.name}</div>
                  <div className="truncate text-sm text-ink-dim">{r.persona?.name ?? r.p.persona_id}</div>
                </div>
                <div className="shrink-0 text-right">
                  <div className="text-lg font-semibold text-accent-soft">Day {r.day}</div>
                  <div className="text-xs tabular-nums text-ink-dim">
                    {r.waitForTomorrow ? "done for today" : `${r.done}/${r.tasks} today`}
                  </div>
                </div>
              </div>

              <div className="mt-3 h-1.5 overflow-hidden rounded-full bg-surface-3">
                <div
                  className="h-full rounded-full bg-linear-to-r from-accent-pale to-accent"
                  style={{ width: `${pct}%` }}
                />
              </div>

              <div className="mt-3 flex flex-wrap gap-x-4 gap-y-1 text-xs text-ink-dim">
                <span>started {r.p.start_date}</span>
                <span>{r.elapsed} days elapsed</span>
                <span>last active {timeAgo(r.last)}</span>
                <span>{r.posted} posted</span>
                <span className={r.low.length ? "font-medium text-warn" : ""}>
                  queue: {r.kinds.map((k) => `${r.queues[k] ?? 0} ${KIND_LABEL[k]}`).join(" · ")}
                  {r.low.length ? " · running low" : ""}
                </span>
                {r.drift > 1 && (
                  <span className="font-medium text-warn">
                    drifting: day {r.day}, started {r.elapsed} days ago
                  </span>
                )}
                {r.drift < 0 && (
                  <span className="font-medium text-accent-soft">
                    {-r.drift} {r.drift === -1 ? "day" : "days"} ahead
                  </span>
                )}
              </div>

              <div className="mt-4 flex items-center gap-2">
                <code className="min-w-0 flex-1 truncate rounded-lg border border-line bg-bg/60 px-3 py-2 font-mono text-xs text-ink-dim">
                  {url}
                </code>
                <CopyButton text={url} label="Copy link" />
                <a
                  href={`/d/${r.p.token}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-quiet shrink-0 rounded-lg px-3 py-2 text-sm font-medium"
                >
                  Open
                </a>
              </div>
            </div>
          );
        })}
        {rows.length === 0 && (
          <p className="text-ink-faint">
            No posters yet. Add one with <code className="font-mono">npm run manage -- add-poster</code>.
          </p>
        )}
      </div>
    </main>
  );
}

function Stat({ label, value, warn }: { label: string; value: number; warn?: boolean }) {
  return (
    <div className="card rounded-2xl px-4 py-3.5">
      <div className={`text-2xl font-semibold tabular-nums ${warn ? "text-warn" : "text-ink"}`}>{value}</div>
      <div className="mt-0.5 text-xs text-ink-dim">{label}</div>
    </div>
  );
}
