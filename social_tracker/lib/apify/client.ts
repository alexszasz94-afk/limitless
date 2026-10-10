/**
 * Minimal Apify API client: start a run, poll it, read its dataset. Never the
 * run-sync endpoints (they time out on slow actors). Actor ids use "~" in
 * paths ("user~name"). The token travels in the Authorization header, never
 * in a URL, so it cannot end up in a log line.
 */

const BASE = "https://api.apify.com/v2";

export interface ApifyLimits {
  monthlyUsageUsd: number;
  maxMonthlyUsageUsd: number;
  /** This key's own billing cycle (every Apify account resets on its own date). */
  cycleStart: string | null;
  cycleEnd: string | null;
  /** Actor runs going on right now on this key. */
  runningNow: number;
}

export interface ApifyRunInfo {
  id: string;
  status: string; // READY | RUNNING | SUCCEEDED | FAILED | ABORTED | TIMED-OUT | TIMING-OUT | ABORTING
  defaultDatasetId: string;
  usageTotalUsd: number | null;
}

export class ApifyError extends Error {
  constructor(
    message: string,
    readonly httpStatus?: number,
    readonly apifyType?: string,
    /** Set when the run had started on Apify (so it was billed and its cost can be read back). */
    readonly runId?: string,
  ) {
    super(message);
  }
}

async function api(token: string, url: string, init?: RequestInit): Promise<unknown> {
  // cache: "no-store": Next.js caches bare GET fetches otherwise (stale key headroom).
  const res = await fetch(url, {
    cache: "no-store",
    ...init,
    headers: { Authorization: `Bearer ${token}`, ...(init?.headers ?? {}) },
    signal: init?.signal ?? AbortSignal.timeout(60_000),
  });
  const text = await res.text();
  let body: unknown = null;
  try {
    body = text ? JSON.parse(text) : null;
  } catch {
    // non-JSON body
  }
  if (!res.ok) {
    const err = (body as { error?: { type?: string; message?: string } } | null)?.error;
    throw new ApifyError(err?.message || `HTTP ${res.status}`, res.status, err?.type);
  }
  return body;
}

export async function getLimits(token: string): Promise<ApifyLimits> {
  const body = (await api(token, `${BASE}/users/me/limits`)) as {
    data: {
      monthlyUsageCycle?: { startAt?: string; endAt?: string };
      current: { monthlyUsageUsd: number; activeActorJobCount?: number };
      limits: { maxMonthlyUsageUsd: number };
    };
  };
  return {
    monthlyUsageUsd: body.data.current.monthlyUsageUsd,
    maxMonthlyUsageUsd: body.data.limits.maxMonthlyUsageUsd,
    cycleStart: body.data.monthlyUsageCycle?.startAt ?? null,
    cycleEnd: body.data.monthlyUsageCycle?.endAt ?? null,
    runningNow: body.data.current.activeActorJobCount ?? 0,
  };
}

export async function getRun(token: string, runId: string): Promise<ApifyRunInfo> {
  const body = (await api(token, `${BASE}/actor-runs/${runId}`)) as {
    data: { id: string; status: string; defaultDatasetId: string; usageTotalUsd?: number };
  };
  return {
    id: body.data.id,
    status: body.data.status,
    defaultDatasetId: body.data.defaultDatasetId,
    usageTotalUsd: typeof body.data.usageTotalUsd === "number" ? body.data.usageTotalUsd : null,
  };
}

const TERMINAL = new Set(["SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"]);

export async function abortRun(token: string, runId: string): Promise<void> {
  await api(token, `${BASE}/actor-runs/${runId}/abort`, { method: "POST" });
}

/**
 * Start a run and wait for it. `onStarted` receives the Apify run id as soon
 * as the run exists (so a crash or restart mid-run can still read its cost
 * back). A run that exceeds timeoutMs, or that can no longer be polled
 * (5 failed polls in a row), is aborted so it cannot keep billing. Every
 * error after the start carries the run id.
 */
export async function runActorAndWait(
  token: string,
  actor: string,
  input: unknown,
  timeoutMs = 300_000,
  onStarted?: (runId: string) => void,
): Promise<{ run: ApifyRunInfo; items: unknown[] }> {
  const started = (await api(token, `${BASE}/acts/${actor}/runs`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(input),
  })) as { data: { id: string } };
  const runId = started.data.id;
  onStarted?.(runId);
  const fail = async (message: string, abort: boolean): Promise<never> => {
    if (abort) {
      try {
        await abortRun(token, runId);
      } catch {
        // best effort
      }
    }
    throw new ApifyError(message, undefined, undefined, runId);
  };
  const deadline = Date.now() + timeoutMs;
  let pollErrors = 0;
  let run: ApifyRunInfo | null = null;
  while (!run || !TERMINAL.has(run.status)) {
    if (Date.now() > deadline)
      await fail(`run ${runId} took longer than ${Math.round(timeoutMs / 1000)} s and was aborted`, true);
    if (run) await new Promise((r) => setTimeout(r, 4000));
    try {
      run = await getRun(token, runId);
      pollErrors = 0;
    } catch (e) {
      if (++pollErrors >= 5)
        await fail(`run ${runId} could not be followed (${e instanceof Error ? e.message : e}) and was aborted`, true);
      await new Promise((r) => setTimeout(r, 4000));
    }
  }
  if (run.status !== "SUCCEEDED") await fail(`run ${runId} ended ${run.status}`, false);
  let items: unknown;
  try {
    items = await api(token, `${BASE}/datasets/${run.defaultDatasetId}/items?clean=false&format=json`);
  } catch (e) {
    await fail(`run ${runId} finished but its results could not be read (${e instanceof Error ? e.message : e})`, false);
  }
  return { run, items: Array.isArray(items) ? items : [] };
}
