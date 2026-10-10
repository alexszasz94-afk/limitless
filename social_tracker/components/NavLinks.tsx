"use client";

import Link from "next/link";
import { usePathname, useSearchParams } from "next/navigation";

const LINKS = [
  { href: "/", label: "Overview" },
  { href: "/videos", label: "Videos" },
  { href: "/runs", label: "Runs" },
  { href: "/keys", label: "Keys" },
];

/** Tabs; the product filter travels with you between pages. */
export default function NavLinks() {
  const path = usePathname();
  const sp = useSearchParams();
  const keep = new URLSearchParams();
  for (const k of ["product", "period"]) {
    const v = sp.get(k);
    if (v) keep.set(k, v);
  }
  const qs = keep.toString();
  return (
    <nav className="scroll-x -mx-1 flex gap-1 px-1" aria-label="Sections">
      {LINKS.map((l) => {
        const active = l.href === "/" ? path === "/" : path.startsWith(l.href);
        const href = l.href === "/runs" || l.href === "/keys" || !qs ? l.href : `${l.href}?${qs}`;
        return (
          <Link
            key={l.href}
            href={href}
            aria-current={active ? "page" : undefined}
            className={`relative shrink-0 rounded-lg px-3 py-2 text-sm font-medium transition-colors ${
              active ? "text-ink" : "text-ink-dim hover:text-ink"
            }`}
          >
            {l.label}
            {active && (
              <span className="absolute inset-x-3 -bottom-[9px] h-[2px] rounded-full bg-accent shadow-[0_0_10px_rgba(77,141,255,0.7)]" />
            )}
          </Link>
        );
      })}
    </nav>
  );
}
