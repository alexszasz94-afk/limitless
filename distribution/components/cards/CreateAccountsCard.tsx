"use client";

import type { CreateAccountsConfig } from "@/lib/config";
import type { Platform } from "@/lib/types";
import { CheckRow, CopyButton, Note, PrimaryButton, SubHead, fmtHandle, useLocalChecks } from "../ui";

export default function CreateAccountsCard({
  config,
  handles,
  scopeKey,
  onComplete,
  done,
}: {
  config: CreateAccountsConfig;
  handles: Record<Platform, string>;
  scopeKey: string;
  onComplete: () => void;
  done: boolean;
}) {
  const { checks, toggle } = useLocalChecks(scopeKey);

  return (
    <div className="flex flex-col gap-6">
      <Note>{config.intro}</Note>

      {config.platforms.map((p) => {
        const handle = handles[p.platform];
        return (
          <div key={p.platform}>
            <SubHead
              aside={
                handle ? (
                  <div className="flex min-w-0 items-center gap-2">
                    <span className="truncate text-sm font-medium text-accent-soft">{fmtHandle(handle)}</span>
                    <CopyButton text={handle} />
                  </div>
                ) : null
              }
            >
              {p.label}
            </SubHead>
            <ul className="flex flex-col gap-3">
              {p.steps.map((step, i) => {
                const id = `${p.platform}_${i}`;
                return (
                  <CheckRow key={id} checked={checks.has(id)} onToggle={() => toggle(id)}>
                    {step}
                  </CheckRow>
                );
              })}
            </ul>
          </div>
        );
      })}

      {!done && <PrimaryButton onClick={onComplete}>Done, all accounts created</PrimaryButton>}
    </div>
  );
}
