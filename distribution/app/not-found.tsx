import Mark from "@/components/Mark";

export default function NotFound() {
  return (
    <main className="flex min-h-dvh flex-col items-center justify-center gap-5 px-8">
      <Mark size={56} />
      <p className="text-center text-sm text-ink-dim">This page doesn&apos;t exist.</p>
    </main>
  );
}
