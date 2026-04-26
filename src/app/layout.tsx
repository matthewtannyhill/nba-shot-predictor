import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: {
    template: "%s | NBA Shot Predictor",
    default: "NBA Shot Predictor",
  },
  description:
    "Two ML models trained on NBA shot tracking and salary data: predict whether a shot goes in, and what a player's salary should be.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full">
      <body className="min-h-full flex flex-col bg-slate-50 text-slate-900 antialiased">
        <header className="bg-slate-900 text-white">
          <nav className="max-w-4xl mx-auto px-6 py-4 flex items-center justify-between">
            <Link href="/" className="font-semibold text-lg">
              NBA Shot Predictor
            </Link>
            <div className="flex gap-6 text-sm">
              <Link href="/shot" className="hover:text-orange-300">
                Shot
              </Link>
              <Link href="/salary" className="hover:text-orange-300">
                Salary
              </Link>
              <Link href="/about" className="hover:text-orange-300">
                About
              </Link>
            </div>
          </nav>
        </header>
        <main className="flex-1">{children}</main>
        <footer className="border-t border-slate-200 py-6 text-center text-sm text-slate-500">
          <a
            href="https://github.com/matthewtannyhill/nba-shot-predictor"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-slate-900"
          >
            github.com/matthewtannyhill/nba-shot-predictor
          </a>
        </footer>
      </body>
    </html>
  );
}
