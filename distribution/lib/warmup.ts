/**
 * Warm-up plan generator.
 *
 * Non-prescriptive by design: the poster gets a list of natural behaviours
 * plus the persona's accounts and keywords, and spends the time behaving like
 * a real user instead of following a scripted sequence.
 *
 * Deterministic per poster per day: the account/keyword ORDER is seeded by
 * poster id + persona + day, so a refresh never reshuffles, and two posters
 * with overlapping lists don't work through them in the same order.
 */
import type { Persona, WarmupPlan } from "./types";
import { seededRng, shuffled } from "./random";
import { getScheduleConfig } from "./config";

export function generateWarmup(posterId: string, persona: Persona, day: number): WarmupPlan {
  const cfg = getScheduleConfig().warmup_defaults;
  const rng = seededRng(`${posterId}:${persona.id}:day${day}:warmup`);
  return {
    perAccountMinutes: cfg.per_account_minutes,
    behaviors: cfg.behaviors ?? [],
    accounts: shuffled(persona.competitors, rng),
    keywords: shuffled(persona.keywords, rng),
  };
}
