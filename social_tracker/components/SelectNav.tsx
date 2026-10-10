"use client";

import { usePathname, useRouter, useSearchParams } from "next/navigation";
import { useTransition } from "react";

/** A filter dropdown that updates one URL parameter (and goes back to page 1). */
export default function SelectNav({
  label,
  param,
  value,
  options,
}: {
  label: string;
  param: string;
  value: string;
  options: Array<{ value: string; label: string }>;
}) {
  const router = useRouter();
  const path = usePathname();
  const sp = useSearchParams();
  const [pending, start] = useTransition();
  return (
    <select
      aria-label={label}
      className={`select ${pending ? "opacity-60" : ""}`}
      value={value}
      onChange={(e) => {
        const next = new URLSearchParams(sp.toString());
        if (e.target.value) next.set(param, e.target.value);
        else next.delete(param);
        next.delete("page");
        const qs = next.toString();
        start(() => router.push(qs ? `${path}?${qs}` : path, { scroll: false }));
      }}
    >
      {options.map((o) => (
        <option key={o.value} value={o.value}>
          {o.label}
        </option>
      ))}
    </select>
  );
}
