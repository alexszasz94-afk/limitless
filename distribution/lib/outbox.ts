"use client";

/**
 * Outbox: every write the poster makes (task done, video posted) goes through
 * here. The UI updates instantly; the request is queued in localStorage and
 * sent in order, retried with backoff while the phone is offline or the
 * server is unreachable, and flushed again on reconnect or next open.
 * Nothing a poster taps is ever silently lost.
 *
 * A 4xx answer means the server refused the write on purpose (e.g. a stale
 * day) and retrying can't help, so it is dropped; 408/425/429 (timeouts and
 * rate limits from a proxy) are retried like network errors.
 */

export interface OutboxItem {
  id: string;
  url: string;
  body: unknown;
}

export interface OutboxState {
  pending: number;
  /** True while requests are failing (offline / server down). */
  stalled: boolean;
}

type Listener = (s: OutboxState) => void;

const listeners = new Set<Listener>();
let key = "";
let queue: OutboxItem[] = [];
let running = false;
let stalled = false;
let retryTimer: ReturnType<typeof setTimeout> | null = null;
let attempt = 0;

const RETRYABLE = new Set([408, 425, 429]);

function save() {
  if (!key) return; // not bound yet: initOutbox saves what was queued
  try {
    if (queue.length) localStorage.setItem(key, JSON.stringify(queue));
    else localStorage.removeItem(key);
  } catch {}
}

function emit() {
  const s = { pending: queue.length, stalled };
  listeners.forEach((l) => l(s));
}

async function run() {
  if (running) return;
  running = true;
  try {
    while (queue.length) {
      const item = queue[0];
      let res: Response | null = null;
      try {
        res = await fetch(item.url, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(item.body),
          keepalive: true,
        });
      } catch {
        res = null;
      }
      if (res && (res.ok || (res.status >= 400 && res.status < 500 && !RETRYABLE.has(res.status)))) {
        queue.shift();
        save();
        attempt = 0;
        if (stalled) stalled = false;
        emit();
        continue;
      }
      // Network error or 5xx: back off and try again later.
      stalled = true;
      emit();
      attempt = Math.min(attempt + 1, 6);
      const wait = Math.min(30000, 1000 * 2 ** (attempt - 1));
      if (retryTimer) clearTimeout(retryTimer);
      retryTimer = setTimeout(() => {
        retryTimer = null;
        void run();
      }, wait);
      break;
    }
  } finally {
    running = false;
  }
}

/** Bind the outbox to one poster (call once on mount). Returns an unsubscribe. */
export function initOutbox(scope: string, onChange: Listener): () => void {
  if (key !== `dist:outbox:${scope}`) {
    key = `dist:outbox:${scope}`;
    let stored: OutboxItem[] = [];
    try {
      const parsed = JSON.parse(localStorage.getItem(key) ?? "[]");
      if (Array.isArray(parsed)) stored = parsed;
    } catch {}
    // Writes sent before binding (a child card can fire first) stay, after
    // the older stored ones, so the order is kept.
    const seen = new Set(stored.map((i) => i.id));
    queue = [...stored, ...queue.filter((i) => !seen.has(i.id))];
    save();
  }
  listeners.add(onChange);
  const kick = () => {
    attempt = 0;
    void run();
  };
  window.addEventListener("online", kick);
  document.addEventListener("visibilitychange", kick);
  onChange({ pending: queue.length, stalled });
  void run();
  return () => {
    listeners.delete(onChange);
    window.removeEventListener("online", kick);
    document.removeEventListener("visibilitychange", kick);
  };
}

/** Writes still waiting to reach the server (read after initOutbox). */
export function pendingItems(): OutboxItem[] {
  return queue.slice();
}

export function send(url: string, body: unknown) {
  queue.push({ id: `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`, url, body });
  save();
  emit();
  if (key) void run(); // before initOutbox the queue only collects; init sends it
}
