"use client";

import type { PlatformInfo, WarmupPlan } from "@/lib/types";
import { CheckRow, CopyButton, Note, PrimaryButton, SubHead, useLocalChecks } from "../ui";

/**
 * Non-prescriptive warm-up: natural behaviours, then the persona's accounts
 * (grouped by platform) and keywords. The poster spends the time acting like
 * a real user instead of following a script. Checks are optional; finishing
 * is never gated.
 */
export default function WarmupCard({
  warmup,
  platforms,
  scopeKey,
  onComplete,
  done,
}: {
  warmup: WarmupPlan;
  platforms: PlatformInfo[];
  scopeKey: string;
  onComplete: () => void;
  done: boolean;
}) {
  const { checks, toggle } = useLocalChecks(scopeKey);

  if (done) return <p className="text-sm text-ink-dim">Warm-up complete.</p>;

  const groups = platforms
    .map((p) => ({ p, accounts: warmup.accounts.filter((a) => a.platform === p.id) }))
    .filter((g) => g.accounts.length > 0);
  const withAccounts = groups.map((g) => g.p.tab_label);
  const withoutAccounts = platforms.filter((p) => !withAccounts.includes(p.tab_label)).map((p) => p.tab_label);

  return (
    <div className="flex flex-col gap-6">
      <Note>
        Spend about <span className="font-semibold text-ink">{warmup.perAccountMinutes} minutes per account</span>{" "}
        behaving like a real user. No script, just do these things naturally:
      </Note>

      <ul className="flex flex-col gap-3">
        {warmup.behaviors.map((b, i) => (
          <CheckRow key={`b${i}`} checked={checks.has(`b${i}`)} onToggle={() => toggle(`b${i}`)}>
            {b}
          </CheckRow>
        ))}
      </ul>

      {groups.map(({ p, accounts }) => (
        <div key={p.id}>
          <SubHead>Accounts to interact with · {p.tab_label}</SubHead>
          <ul className="flex flex-col gap-2">
            {accounts.map((a) => (
              <li
                key={`${a.platform}_${a.handle}`}
                className="flex items-center justify-between gap-3 rounded-xl border border-line bg-surface-2/60 px-4 py-2.5"
              >
                <span className="min-w-0 truncate text-[15px]">@{a.handle}</span>
                <CopyButton text={a.handle} />
              </li>
            ))}
          </ul>
        </div>
      ))}

      {warmup.keywords.length > 0 && (
        <div>
          <SubHead>Keywords to search · every platform</SubHead>
          {withoutAccounts.length > 0 && (
            <p className="mb-2.5 text-xs leading-snug text-ink-faint">
              {withoutAccounts.join(", ")} {withoutAccounts.length > 1 ? "have" : "has"} no account list: search
              these and interact with what comes up.
            </p>
          )}
          <div className="flex flex-wrap gap-2">
            {warmup.keywords.map((k) => (
              <span key={k} className="rounded-full border border-line bg-surface-2/60 px-3 py-1.5 text-sm text-ink-dim">
                {k}
              </span>
            ))}
          </div>
        </div>
      )}

      <PrimaryButton onClick={onComplete}>Finish warm-up</PrimaryButton>
    </div>
  );
}
