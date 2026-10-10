import type { Metadata, Viewport } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "Social Tracker", template: "%s · Social Tracker" },
  description: "Views, posts and followers of every product",
  applicationName: "Social Tracker",
  manifest: "/manifest.webmanifest",
  robots: { index: false, follow: false, nocache: true },
  referrer: "no-referrer",
  appleWebApp: { capable: true, statusBarStyle: "black-translucent", title: "Tracker" },
  formatDetection: { telephone: false },
};

export const viewport: Viewport = {
  themeColor: "#0e1014",
  colorScheme: "dark",
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
