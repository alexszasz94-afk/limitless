import Link from "next/link";
import { fmtCompact, fmtFull, fmtPct } from "@/lib/format";

/** Up/down change badge. Text says the direction; colour only supports it. */
export function Change({ value, suffix }: { value: number | null; suffix?: string }) {
  if (value === null) return <span className="text-xs text-ink-faint">{suffix ? `– ${suffix}` : "–"}</span>;
  const up = value > 0;
  const flat = Math.abs(value) < 0.05;
  return (
    <span
      className={`inline-flex items-center gap-1 text-xs font-medium ${flat ? "text-ink-faint" : up ? "text-good" : "text-bad"}`}
    >
      {!flat && (
        <svg
          width="10"
          height="10"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="3"
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
          style={{ transform: up ? undefined : "rotate(180deg)" }}
        >
          <path d="M12 19V5M5 12l7-7 7 7" />
        </svg>
      )}
      {fmtPct(value)}
      {suffix && <span className="font-normal text-ink-faint">{suffix}</span>}
    </span>
  );
}

/** A number shown compact, with the exact figure on hover. */
export function N({ v, className = "" }: { v: number | null | undefined; className?: string }) {
  return (
    <span className={`num ${className}`} title={v === null || v === undefined ? undefined : fmtFull(v)}>
      {fmtCompact(v)}
    </span>
  );
}

export function PageHeader({ title, sub, children }: { title: string; sub?: React.ReactNode; children?: React.ReactNode }) {
  return (
    <div className="mb-6 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
      <div className="min-w-0">
        <h1 className="text-2xl font-semibold tracking-tight sm:text-[28px]">{title}</h1>
        {sub && <p className="mt-1 text-sm text-ink-dim">{sub}</p>}
      </div>
      {children}
    </div>
  );
}

export function Chips({
  items,
  label,
}: {
  items: Array<{ key: string; label: React.ReactNode; href: string; active: boolean }>;
  label: string;
}) {
  return (
    <div className="scroll-x -mx-4 px-4 sm:mx-0 sm:px-0" role="group" aria-label={label}>
      <div className="flex w-max gap-1.5">
        {items.map((i) => (
          <Link key={i.key} href={i.href} className="chip" aria-current={i.active ? "true" : undefined} scroll={false}>
            {i.label}
          </Link>
        ))}
      </div>
    </div>
  );
}

export function Card({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  return <section className={`card rounded-2xl ${className}`}>{children}</section>;
}

export function CardHead({ title, aside, sub }: { title: string; aside?: React.ReactNode; sub?: React.ReactNode }) {
  return (
    <div className="flex items-start justify-between gap-3 px-5 pt-4">
      <div className="min-w-0">
        <h2 className="text-[15px] font-semibold tracking-tight">{title}</h2>
        {sub && <p className="mt-0.5 text-xs text-ink-faint">{sub}</p>}
      </div>
      {aside}
    </div>
  );
}

export function Empty({ title, children }: { title: string; children?: React.ReactNode }) {
  return (
    <div className="flex flex-col items-center px-6 py-10 text-center">
      <div className="mb-3 flex h-10 w-10 items-center justify-center rounded-full border border-line bg-surface-2 text-ink-faint">
        <svg
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
        >
          <circle cx="12" cy="12" r="9" />
          <path d="M12 7v5l3 2" />
        </svg>
      </div>
      <p className="text-sm font-medium text-ink">{title}</p>
      {children && <div className="mt-1 max-w-md text-sm text-ink-dim">{children}</div>}
    </div>
  );
}

export function ExternalIcon() {
  return (
    <svg
      width="11"
      height="11"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2.4"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      className="shrink-0 opacity-60"
    >
      <path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5" />
    </svg>
  );
}
