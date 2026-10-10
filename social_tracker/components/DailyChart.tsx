"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import type { Platform } from "@/lib/config";

/**
 * Views gained per day, stacked by platform. Hand-drawn SVG (no chart
 * library): 2 px surface gaps between segments, rounded data-ends, recessive
 * grid, a hover/tap tooltip per day, and a table view underneath.
 * Negative days (a platform revising a count down) are drawn at 0 and shown
 * exactly in the tooltip and table.
 */

export interface ChartPoint {
  date: string;
  values: Record<Platform, number>;
}

const LABEL: Record<Platform, string> = { instagram: "Instagram", tiktok: "TikTok", facebook: "Facebook" };
const HEX: Record<Platform, string> = { instagram: "#d95926", tiktok: "#199e8c", facebook: "#4d8dff" };
const ORDER: Platform[] = ["instagram", "tiktok", "facebook"];

function compact(n: number): string {
  const a = Math.abs(n);
  const s = n < 0 ? "−" : "";
  if (a >= 1e6) return `${s}${(a / 1e6).toFixed(a >= 1e7 ? 0 : 1).replace(/\.0$/, "")}M`;
  if (a >= 1e3) return `${s}${(a / 1e3).toFixed(a >= 1e4 ? 0 : 1).replace(/\.0$/, "")}K`;
  return `${s}${Math.round(a)}`;
}

function niceMax(v: number): { max: number; step: number } {
  if (v <= 0) return { max: 4, step: 1 };
  const raw = v / 4;
  const mag = Math.pow(10, Math.floor(Math.log10(raw)));
  const norm = raw / mag;
  const step = (norm <= 1 ? 1 : norm <= 2 ? 2 : norm <= 2.5 ? 2.5 : norm <= 5 ? 5 : 10) * mag;
  return { max: step * 4, step };
}

// Formatted by hand, not with Intl: the server's and the browser's ICU
// differ ("Tue 6 Oct" vs "Tue, 6 Oct") and would break hydration.
const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

function dayLabel(date: string, withWeekday = false): string {
  const [y, m, d] = date.split("-").map(Number);
  const label = `${d} ${MONTHS[m - 1]}`;
  return withWeekday ? `${WEEKDAYS[new Date(Date.UTC(y, m - 1, d)).getUTCDay()]} ${label}` : label;
}

function full(n: number): string {
  const r = Math.round(n);
  return (r < 0 ? "−" : "") + String(Math.abs(r)).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

/** A bar segment with only its top corners rounded. */
function topRounded(x: number, y: number, w: number, h: number, r: number): string {
  const rr = Math.min(r, w / 2, h);
  return `M${x},${y + h} V${y + rr} Q${x},${y} ${x + rr},${y} H${x + w - rr} Q${x + w},${y} ${x + w},${y + rr} V${y + h} Z`;
}

export default function DailyChart({ points, platforms = ORDER }: { points: ChartPoint[]; platforms?: Platform[] }) {
  const wrap = useRef<HTMLDivElement>(null);
  const [width, setWidth] = useState(0);
  const [hover, setHover] = useState<number | null>(null);

  useEffect(() => {
    const el = wrap.current;
    if (!el) return;
    const ro = new ResizeObserver(([e]) => setWidth(Math.floor(e.contentRect.width)));
    ro.observe(el);
    setWidth(Math.floor(el.getBoundingClientRect().width));
    return () => ro.disconnect();
  }, []);

  const height = width < 520 ? 210 : 260;
  const pad = { top: 12, right: 4, bottom: 26, left: 40 };
  const plotW = Math.max(0, width - pad.left - pad.right);
  const plotH = height - pad.top - pad.bottom;

  const totals = useMemo(
    () => points.map((p) => platforms.reduce((s, k) => s + Math.max(0, p.values[k] ?? 0), 0)),
    [points, platforms],
  );
  const { max, step } = niceMax(Math.max(0, ...totals));
  const empty = totals.every((t) => t === 0);
  const n = points.length;
  const band = n ? plotW / n : 0;
  const barW = Math.max(2, Math.min(28, band * (n > 60 ? 0.78 : 0.62)));
  const y = (v: number) => pad.top + plotH - (v / max) * plotH;
  const labelEvery = Math.max(1, Math.ceil(n / Math.max(2, Math.floor(plotW / 64))));

  const tip = hover !== null ? points[hover] : null;
  const tipLeft = hover !== null ? pad.left + band * (hover + 0.5) : 0;

  return (
    <div>
      <div ref={wrap} className="relative w-full select-none" style={{ height }} onMouseLeave={() => setHover(null)}>
        {width > 0 && (
          <svg width={width} height={height} role="img" aria-label="Views gained per day, by platform">
            {Array.from({ length: 5 }, (_, i) => i * step).map((v) => (
              <g key={v}>
                <line
                  x1={pad.left}
                  x2={width - pad.right}
                  y1={y(v)}
                  y2={y(v)}
                  stroke="#252d3b"
                  strokeDasharray={v === 0 ? undefined : "2 4"}
                />
                <text x={pad.left - 8} y={y(v)} dy="0.32em" textAnchor="end" fontSize="11" fill="#5f6a80" className="num">
                  {compact(v)}
                </text>
              </g>
            ))}
            {points.map((p, i) => {
              const x = pad.left + band * i + (band - barW) / 2;
              let acc = 0;
              const segs = platforms.map((k) => ({ k, v: Math.max(0, p.values[k] ?? 0) })).filter((s) => s.v > 0);
              return (
                <g key={p.date} opacity={hover === null || hover === i ? 1 : 0.45}>
                  {segs.map((s, j) => {
                    const y0 = y(acc);
                    acc += s.v;
                    const y1 = y(acc);
                    // 2 px surface gap: every segment above the first gives up its bottom 2 px.
                    const h = Math.max(1.5, y0 - y1 - (j > 0 ? 2 : 0));
                    return j === segs.length - 1 ? (
                      <path key={s.k} d={topRounded(x, y1, barW, h, 4)} fill={HEX[s.k]} />
                    ) : (
                      <rect key={s.k} x={x} y={y1} width={barW} height={h} fill={HEX[s.k]} />
                    );
                  })}
                </g>
              );
            })}
            {points.map((p, i) =>
              (n - 1 - i) % labelEvery === 0
                ? (() => {
                    // Keep edge labels inside the chart instead of clipping them.
                    const cx = pad.left + band * (i + 0.5);
                    const anchor = cx + 22 > width ? "end" : cx - 22 < 0 ? "start" : "middle";
                    const x = anchor === "end" ? width - 1 : anchor === "start" ? 1 : cx;
                    return (
                      <text key={p.date} x={x} y={height - 8} textAnchor={anchor} fontSize="11" fill="#5f6a80">
                        {dayLabel(p.date)}
                      </text>
                    );
                  })()
                : null,
            )}
            {points.map((p, i) => (
              <rect
                key={p.date}
                x={pad.left + band * i}
                y={pad.top}
                width={band}
                height={plotH}
                fill="transparent"
                onMouseEnter={() => setHover(i)}
                onClick={() => setHover(i)}
              />
            ))}
          </svg>
        )}
        {empty && width > 0 && (
          <div className="pointer-events-none absolute inset-0 flex items-center justify-center pb-6 pl-10">
            <p className="rounded-lg bg-bg/70 px-3 py-1.5 text-sm text-ink-faint">No views gained in this period yet</p>
          </div>
        )}
        {tip && !empty && (
          <div
            className="pointer-events-none absolute top-1 z-10 w-44 rounded-xl border border-line-strong bg-surface-2/95 p-3 text-xs shadow-[0_12px_30px_-10px_rgba(0,0,0,0.8)] backdrop-blur"
            style={{ left: Math.min(Math.max(tipLeft - 88, 0), Math.max(0, width - 176)) }}
          >
            <p className="mb-2 font-semibold text-ink">{dayLabel(tip.date, true)}</p>
            {platforms.map((k) => (
              <p key={k} className="flex items-center justify-between gap-2 py-0.5 text-ink-dim">
                <span className="flex items-center gap-1.5">
                  <span className="dot" style={{ background: HEX[k] }} />
                  {LABEL[k]}
                </span>
                <span className="num text-ink">{full(tip.values[k] ?? 0)}</span>
              </p>
            ))}
            <p className="mt-1.5 flex justify-between border-t border-line pt-1.5 font-medium text-ink">
              <span>Total</span>
              <span className="num">{full(platforms.reduce((s, k) => s + (tip.values[k] ?? 0), 0))}</span>
            </p>
          </div>
        )}
      </div>
      <details className="mt-3 text-sm">
        <summary className="cursor-pointer select-none text-xs text-ink-faint hover:text-ink-dim">Show as table</summary>
        <div className="scroll-x mt-2 max-h-72 overflow-y-auto rounded-xl border border-line">
          <table className="table">
            <thead>
              <tr>
                <th>Day</th>
                {platforms.map((k) => (
                  <th key={k} className="r">
                    {LABEL[k]}
                  </th>
                ))}
                <th className="r">Total</th>
              </tr>
            </thead>
            <tbody>
              {[...points].reverse().map((p) => (
                <tr key={p.date}>
                  <td className="whitespace-nowrap text-ink-dim">{dayLabel(p.date, true)}</td>
                  {platforms.map((k) => (
                    <td key={k} className="r">
                      {full(p.values[k] ?? 0)}
                    </td>
                  ))}
                  <td className="r font-medium">{full(platforms.reduce((s, k) => s + (p.values[k] ?? 0), 0))}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </details>
    </div>
  );
}
