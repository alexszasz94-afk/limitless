/** The app mark: a dark tile with the blue glow and broadcast glyph. */
export default function Mark({ size = 40, className = "" }: { size?: number; className?: string }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 64 64"
      aria-hidden="true"
      className={className}
    >
      <defs>
        <radialGradient id="mark-glow">
          <stop stopColor="#4D8DFF" stopOpacity=".42" />
          <stop offset="1" stopColor="#4D8DFF" stopOpacity="0" />
        </radialGradient>
      </defs>
      <rect width="64" height="64" rx="15" fill="#0E1014" />
      <rect x=".75" y=".75" width="62.5" height="62.5" rx="14.4" fill="none" stroke="#fff" strokeOpacity=".1" strokeWidth="1.5" />
      <circle cx="32" cy="32" r="28" fill="url(#mark-glow)" />
      <g transform="translate(32 32) scale(.9) translate(-32 -32)">
        <path
          d="M28.5 25.2v13.6c0 1.2 1.3 1.9 2.3 1.3l10.6-6.8c.9-.6.9-2 0-2.6l-10.6-6.8c-1-.6-2.3.1-2.3 1.3z"
          fill="#79ADFF"
          stroke="#79ADFF"
          strokeWidth="2.2"
          strokeLinejoin="round"
          transform="translate(-1.6 0)"
        />
        <g fill="none" stroke="#79ADFF" strokeWidth="3.8" strokeLinecap="round">
          <path d="M20.5 22.5a14 14 0 0 0 0 19" />
          <path d="M43.5 22.5a14 14 0 0 1 0 19" />
          <path d="M13.5 16.5a23 23 0 0 0 0 31" />
          <path d="M50.5 16.5a23 23 0 0 1 0 31" />
        </g>
      </g>
    </svg>
  );
}
