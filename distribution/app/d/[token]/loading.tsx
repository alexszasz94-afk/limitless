/** Skeleton while the day manifest is resolved on the server. */
export default function Loading() {
  return (
    <main className="mx-auto max-w-md px-4 pt-[calc(1.75rem+env(safe-area-inset-top))]" aria-busy="true">
      <div className="mb-7 flex items-center justify-between px-1">
        <div>
          <div className="skeleton mb-3 h-4 w-32 rounded" />
          <div className="skeleton h-9 w-28 rounded-lg" />
          <div className="skeleton mt-3 h-4 w-20 rounded" />
        </div>
        <div className="skeleton h-[76px] w-[76px] rounded-full" />
      </div>
      <div className="flex flex-col gap-3">
        <div className="skeleton h-14 rounded-2xl" />
        <div className="skeleton h-[420px] rounded-2xl" />
        <div className="skeleton h-14 rounded-2xl" />
      </div>
    </main>
  );
}
