"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import type { DayManifest, PlatformInfo, ResolvedTask } from "@/lib/types";
import type { CreateAccountsConfig, PrivacyConfig } from "@/lib/config";
import { initOutbox, pendingItems, send, type OutboxState } from "@/lib/outbox";
import ProgressRing from "./ProgressRing";
import Mark from "./Mark";
import { PrimaryButton } from "./ui";
import CreateAccountsCard from "./cards/CreateAccountsCard";
import PrivacyLockdownCard from "./cards/PrivacyLockdownCard";
import WarmupCard from "./cards/WarmupCard";
import ProfileSetupCard from "./cards/ProfileSetupCard";
import PostMediaCard from "./cards/PostMediaCard";

export interface CardConfigs {
  privacy: PrivacyConfig;
  createAccounts: CreateAccountsConfig;
  platforms: PlatformInfo[];
}

const TASK_TITLES: Record<string, string> = {
  create_accounts: "Create the accounts",
  privacy_lockdown: "Privacy lockdown",
  warmup: "Warm-up",
  profile_setup: "Set up the profiles",
  post_reel: "Post a reel",
  post_story: "Post a story",
  add_highlight: "Update highlights",
};

export default function DayView({
  token,
  manifest,
  configs,
}: {
  token: string;
  manifest: DayManifest;
  configs: CardConfigs;
}) {
  const [completed, setCompleted] = useState<Set<number>>(
    () => new Set(manifest.tasks.filter((t) => t.completed).map((t) => t.index)),
  );
  // A day already finished today opens straight on the finish screen.
  const [celebrate, setCelebrate] = useState(manifest.waitForTomorrow);
  const [sync, setSync] = useState<OutboxState>({ pending: 0, stalled: false });
  const [opening, setOpening] = useState(false);
  const celebrateTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  const total = manifest.tasks.length;
  const done = completed.size;
  const allDone = total > 0 && done >= total;

  // Writes go through the outbox (queued, retried, never lost). Ticks that
  // were still queued from an earlier visit count as done right away.
  useEffect(() => {
    const off = initOutbox(token, setSync);
    const queued = pendingItems()
      .filter((i) => i.url.endsWith("/progress"))
      .map((i) => i.body as { day: number; taskIndex: number; completed?: boolean })
      .filter((b) => b.day === manifest.day && b.completed !== false)
      .map((b) => b.taskIndex);
    if (queued.length) setCompleted((prev) => new Set([...prev, ...queued]));
    return () => {
      off();
      if (celebrateTimer.current) clearTimeout(celebrateTimer.current);
    };
  }, [token, manifest.day]);

  const markDone = useCallback(
    (taskIndex: number) => {
      setCompleted((prev) => {
        if (prev.has(taskIndex)) return prev;
        const next = new Set(prev);
        next.add(taskIndex);
        if (next.size >= total) celebrateTimer.current = setTimeout(() => setCelebrate(true), 1500);
        return next;
      });
      send(`/api/poster/${token}/progress`, { day: manifest.day, taskIndex, at: new Date().toISOString() });
    },
    [token, manifest.day, total],
  );

  const totals: Record<string, number> = {};
  for (const t of manifest.tasks) totals[t.type] = (totals[t.type] ?? 0) + 1;
  const seen: Record<string, number> = {};

  if (celebrate) {
    return (
      <main className="flex min-h-dvh flex-col items-center justify-center px-8 text-center">
        <div className="relative animate-pop">
          <div className="finish-glow" />
          <ProgressRing done={1} total={1} size={120} />
        </div>
        <h1 className="mt-10 text-3xl font-semibold tracking-tight animate-fade-up">Day {manifest.day} done.</h1>
        <p className="mt-2 max-w-xs text-ink-dim animate-fade-up">
          {manifest.oneDayPerCalendarDay
            ? `That's everything for today. Day ${manifest.day + 1} opens tomorrow.`
            : `Keep the momentum and start day ${manifest.day + 1} now, or come back to it later.`}
        </p>
        <SyncPill sync={sync} className="mt-6" />
        <div className="mt-10 flex w-full max-w-xs flex-col items-center gap-2 pb-[env(safe-area-inset-bottom)]">
          {!manifest.oneDayPerCalendarDay && (
            <PrimaryButton
              big
              disabled={sync.pending > 0 || opening}
              onClick={() => {
                setOpening(true);
                location.reload();
              }}
            >
              {sync.pending > 0 ? "Saving…" : opening ? "Opening…" : `Start day ${manifest.day + 1}`}
            </PrimaryButton>
          )}
          <button
            type="button"
            onClick={() => setCelebrate(false)}
            className="min-h-11 px-4 text-sm text-ink-faint"
          >
            Look at day {manifest.day}&apos;s tasks
          </button>
        </div>
      </main>
    );
  }

  return (
    <main className="mx-auto max-w-md px-4 pb-[calc(6rem+env(safe-area-inset-bottom))] pt-[calc(1.75rem+env(safe-area-inset-top))]">
      <header className="mb-7 flex items-center justify-between gap-4 px-1">
        <div className="min-w-0">
          <div className="mb-2 flex items-center gap-2">
            <Mark size={22} />
            <p className="truncate text-sm font-medium text-ink-dim">{manifest.personaName}</p>
          </div>
          <h1 className="text-[34px] font-semibold leading-none tracking-tight">Day {manifest.day}</h1>
          <div className="mt-2.5 flex items-center gap-2">
            <p className="text-sm text-ink-faint">
              {allDone ? "All done" : `${total - done} ${total - done === 1 ? "task" : "tasks"} left`}
            </p>
            <SyncPill sync={sync} />
          </div>
        </div>
        <ProgressRing done={done} total={total} size={76} />
      </header>

      <div className="flex flex-col gap-3">
        {manifest.tasks.map((task) => {
          seen[task.type] = (seen[task.type] ?? 0) + 1;
          const base = TASK_TITLES[task.type] ?? task.type;
          const title = totals[task.type] > 1 ? `${base} (${seen[task.type]} of ${totals[task.type]})` : base;
          return (
            <TaskShell key={task.index} n={task.index + 1} title={title} done={completed.has(task.index)}>
              <CardBody
                task={task}
                token={token}
                day={manifest.day}
                manifest={manifest}
                configs={configs}
                done={completed.has(task.index)}
                onComplete={() => markDone(task.index)}
              />
            </TaskShell>
          );
        })}
        {total === 0 && (
          <p className="card rounded-2xl p-5 text-sm text-ink-dim">Nothing scheduled for today.</p>
        )}
      </div>

      {allDone && (
        <div className="mt-6">
          <PrimaryButton big onClick={() => setCelebrate(true)}>
            Finish the day
          </PrimaryButton>
        </div>
      )}
    </main>
  );
}

/** Small status chip: only visible while something is still syncing. */
function SyncPill({ sync, className = "" }: { sync: OutboxState; className?: string }) {
  if (!sync.pending) return null;
  return (
    <span
      className={`inline-flex items-center gap-1.5 rounded-full border px-2 py-0.5 text-[11px] font-medium ${
        sync.stalled ? "border-warn/40 bg-warn/10 text-warn" : "border-line bg-surface-2 text-ink-dim"
      } ${className}`}
      role="status"
    >
      <span className={`h-1.5 w-1.5 rounded-full ${sync.stalled ? "bg-warn" : "animate-pulse bg-accent"}`} />
      {sync.stalled ? "Offline, will sync" : "Saving…"}
    </span>
  );
}

// Particle burst for the just-completed check (dx/dy in px).
const BURST = [
  { dx: -22, dy: -18, c: "#4D8DFF", delay: 0 },
  { dx: 22, dy: -20, c: "#A8C8FF", delay: 40 },
  { dx: 27, dy: 5, c: "#79ADFF", delay: 20 },
  { dx: -26, dy: 3, c: "#A8C8FF", delay: 60 },
  { dx: -14, dy: 21, c: "#4D8DFF", delay: 80 },
  { dx: 14, dy: 24, c: "#EEF2FA", delay: 30 },
  { dx: 6, dy: -24, c: "#79ADFF", delay: 10 },
  { dx: -6, dy: 26, c: "#A8C8FF", delay: 70 },
  { dx: 0, dy: -26, c: "#4D8DFF", delay: 50 },
];

/** Completed tasks collapse to a slim confirmation row. */
function TaskShell({
  n,
  title,
  done,
  children,
}: {
  n: number;
  title: string;
  done: boolean;
  children: React.ReactNode;
}) {
  const [expanded, setExpanded] = useState(false);
  // Celebrate only a task completed in THIS session (done flips false -> true).
  const [justDone, setJustDone] = useState(false);
  const prevDone = useRef(done);
  const rowRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    if (done && !prevDone.current) {
      prevDone.current = done;
      setJustDone(true);
      setExpanded(false);
      // A tall card collapsing can leave this row above the viewport; bring it into view.
      requestAnimationFrame(() => rowRef.current?.scrollIntoView({ behavior: "smooth", block: "center" }));
      const t = setTimeout(() => setJustDone(false), 1100);
      return () => clearTimeout(t);
    }
    prevDone.current = done;
  }, [done]);

  if (done && !expanded) {
    return (
      <button
        ref={rowRef}
        type="button"
        onClick={() => setExpanded(true)}
        className={`card flex w-full items-center gap-3 rounded-2xl px-5 py-3.5 text-left transition-opacity ${
          justDone ? "animate-task-done opacity-100" : "opacity-75 hover:opacity-100"
        }`}
      >
        <span
          className={`relative flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-accent ${
            justDone ? "animate-check-pop" : ""
          }`}
        >
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#0e1014" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
            <path d="M20 6L9 17l-5-5" className={justDone ? "check-draw" : undefined} />
          </svg>
          {justDone && <i className="ring-pulse" />}
          {justDone &&
            BURST.map((b, i) => (
              <i
                key={i}
                className="burst-dot"
                style={
                  {
                    "--dx": `${b.dx}px`,
                    "--dy": `${b.dy}px`,
                    background: b.c,
                    animationDelay: `${b.delay}ms`,
                  } as React.CSSProperties
                }
              />
            ))}
        </span>
        <span className="flex-1 text-sm text-ink-dim line-through decoration-ink-faint">{title}</span>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-ink-faint" aria-hidden="true">
          <path d="M6 9l6 6 6-6" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </button>
    );
  }

  return (
    <section className="card animate-fade-up rounded-2xl p-5">
      <div className="mb-5 flex items-center gap-3">
        <span
          className={`flex h-7 w-7 shrink-0 items-center justify-center rounded-lg text-[13px] font-bold ${
            done ? "bg-accent text-bg" : "bg-accent/15 text-accent-soft"
          }`}
        >
          {n}
        </span>
        <h2 className="flex-1 text-lg font-semibold tracking-tight">{title}</h2>
        {done && (
          <button type="button" onClick={() => setExpanded(false)} className="text-xs font-medium text-ink-faint">
            Collapse
          </button>
        )}
      </div>
      {children}
    </section>
  );
}

function CardBody({
  task,
  token,
  day,
  manifest,
  configs,
  done,
  onComplete,
}: {
  task: ResolvedTask;
  token: string;
  day: number;
  manifest: DayManifest;
  configs: CardConfigs;
  done: boolean;
  onComplete: () => void;
}) {
  const scope = `dist:${token}:d${day}:${manifest.openedAt}:t${task.index}`;
  switch (task.type) {
    case "create_accounts":
      return (
        <CreateAccountsCard
          config={configs.createAccounts}
          handles={manifest.handles}
          scopeKey={scope}
          onComplete={onComplete}
          done={done}
        />
      );
    case "privacy_lockdown":
      return <PrivacyLockdownCard config={configs.privacy} scopeKey={scope} onComplete={onComplete} done={done} />;
    case "warmup":
      return (
        <WarmupCard
          warmup={task.warmup!}
          platforms={configs.platforms}
          scopeKey={scope}
          onComplete={onComplete}
          done={done}
        />
      );
    case "profile_setup":
      return (
        <ProfileSetupCard
          token={token}
          personaId={manifest.personaId}
          bio={manifest.bio}
          handles={manifest.handles}
          platforms={configs.platforms}
          scopeKey={scope}
          onComplete={onComplete}
          done={done}
        />
      );
    case "post_reel":
    case "post_story":
    case "add_highlight":
      return (
        <PostMediaCard
          token={token}
          platforms={configs.platforms}
          pinnedComment={task.content?.suppress_pinned_comment ? undefined : manifest.pinnedComment}
          content={task.content ?? null}
          onComplete={onComplete}
          done={done}
        />
      );
    default:
      return <PrimaryButton onClick={onComplete}>Mark done</PrimaryButton>;
  }
}
