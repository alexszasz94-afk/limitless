/** The app mark: a dark tile with the blue glow and a rising-trend glyph. */
export default function Mark({ size = 40, className = "" }: { size?: number; className?: string }) {
  return (
    <svg width={size} height={size} viewBox="0 0 64 64" aria-hidden="true" className={className}>
      <defs>
        <radialGradient id="mark-glow">
          <stop stopColor="#4D8DFF" stopOpacity=".42" />
          <stop offset="1" stopColor="#4D8DFF" stopOpacity="0" />
        </radialGradient>
      </defs>
      <rect width="64" height="64" rx="15" fill="#0E1014" />
      <rect x=".75" y=".75" width="62.5" height="62.5" rx="14.4" fill="none" stroke="#fff" strokeOpacity=".1" strokeWidth="1.5" />
      <circle cx="32" cy="32" r="28" fill="url(#mark-glow)" />
      <g
        transform="translate(32 32) scale(.9) translate(-32 -32)"
        fill="none"
        stroke="#79ADFF"
        strokeWidth="4"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d="M13 43 L25.5 30.5 L34 38 L50 22" />
        <path d="M41 22 H50 V31" />
      </g>
    </svg>
  );
}
