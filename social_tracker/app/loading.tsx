export default function Loading() {
  return (
    <div className="mx-auto max-w-6xl px-4 pt-24 sm:px-6">
      <div className="skeleton mb-4 h-8 w-48 rounded-lg" />
      <div className="skeleton mb-4 h-40 rounded-2xl" />
      <div className="skeleton h-72 rounded-2xl" />
    </div>
  );
}
