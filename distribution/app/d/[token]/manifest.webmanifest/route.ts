import { getPosterByToken } from "@/lib/db";

/**
 * Per-poster web app manifest: "Add to Home Screen" from a poster's page
 * installs an app that opens straight on THEIR day (start_url carries the
 * token), instead of the empty home page.
 */
export async function GET(_req: Request, { params }: { params: Promise<{ token: string }> }) {
  const { token } = await params;
  if (!getPosterByToken(token)) return new Response("Not found", { status: 404 });
  const manifest = {
    name: "Distribution",
    short_name: "Distribution",
    description: "Daily posting checklist",
    id: `/d/${token}`,
    start_url: `/d/${token}`,
    scope: `/d/${token}`,
    display: "standalone",
    orientation: "portrait",
    background_color: "#0e1014",
    theme_color: "#0e1014",
    icons: [
      { src: "/icons/icon-192.png", sizes: "192x192", type: "image/png", purpose: "any" },
      { src: "/icons/icon-512.png", sizes: "512x512", type: "image/png", purpose: "any" },
      { src: "/icons/icon-maskable-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
    ],
  };
  return new Response(JSON.stringify(manifest), {
    headers: { "Content-Type": "application/manifest+json", "Cache-Control": "private, no-cache" },
  });
}
