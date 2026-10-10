import Mark from "@/components/Mark";

export default function Home() {
  return (
    <main className="flex min-h-dvh flex-col items-center justify-center gap-5 px-8">
      <Mark size={56} />
      <p className="text-center text-sm text-ink-dim">
        Nothing here. Open the link you were given.
      </p>
    </main>
  );
}
