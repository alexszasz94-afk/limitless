"use client";

import type { PrivacyConfig } from "@/lib/config";
import { Check, Note, PrimaryButton, useLocalChecks } from "../ui";

export default function PrivacyLockdownCard({
  config,
  scopeKey,
  onComplete,
  done,
}: {
  config: PrivacyConfig;
  scopeKey: string;
  onComplete: () => void;
  done: boolean;
}) {
  const { checks, toggle } = useLocalChecks(scopeKey);

  return (
    <div className="flex flex-col gap-5">
      <Note>{config.page_note}</Note>

      <ul className="flex flex-col gap-5">
        {config.items.map((item) => {
          const on = checks.has(item.id);
          return (
            <li key={item.id} className="flex items-start gap-3">
              <Check checked={on} onToggle={() => toggle(item.id)} size={24} label={item.title} />
              <div className="min-w-0">
                <div className="flex flex-wrap items-center gap-2">
                  <span
                    className={`text-[15px] font-medium leading-snug ${
                      on ? "text-ink-faint line-through decoration-ink-faint" : ""
                    }`}
                  >
                    {item.title}
                  </span>
                  <span
                    className={`rounded-md px-1.5 py-0.5 text-[10px] font-bold uppercase tracking-wider ${
                      item.mode === "do"
                        ? "bg-accent/15 text-accent-soft"
                        : "bg-surface-3 text-ink-dim"
                    }`}
                  >
                    {item.mode === "do" ? "do this" : "deny"}
                  </span>
                </div>
                <p className="mt-1 text-sm leading-relaxed text-ink-dim">{item.detail}</p>
                <p className="mt-1 text-[11px] text-ink-faint">
                  checked {item.verified_on}
                  {item.needs_verification ? " · menus may have changed, look for the closest option" : ""}
                </p>
              </div>
            </li>
          );
        })}
      </ul>

      {!done && <PrimaryButton onClick={onComplete}>Done, locked down</PrimaryButton>}
    </div>
  );
}
