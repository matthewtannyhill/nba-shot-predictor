import Link from "next/link";

export default function Home() {
  return (
    <div className="max-w-4xl mx-auto px-6 py-16">
      <h1 className="text-4xl font-bold mb-4">NBA Shot Predictor</h1>
      <p className="text-lg text-slate-600 mb-12 max-w-2xl">
        Two scikit-learn models trained on public NBA datasets. Originally a 2019 BYU
        class project that called Azure ML Studio (retired by Microsoft in 2024);
        modernized in 2026 with locally-trained random forests.
      </p>

      <div className="grid md:grid-cols-2 gap-6">
        <Link
          href="/shot"
          className="block p-8 bg-white rounded-xl border border-slate-200 hover:border-orange-400 hover:shadow-md transition"
        >
          <div className="text-sm font-medium text-orange-600 mb-2">Model 1</div>
          <h2 className="text-2xl font-semibold mb-3">Shot Outcome</h2>
          <p className="text-slate-600 text-sm">
            Given pre-shot tracking features (shot clock, distance, defender, dribbles),
            predict the probability the shot goes in.
          </p>
          <p className="text-xs text-slate-400 mt-4">
            Trained on 128k shots from the 2014-15 season. AUC 0.634.
          </p>
        </Link>

        <Link
          href="/salary"
          className="block p-8 bg-white rounded-xl border border-slate-200 hover:border-orange-400 hover:shadow-md transition"
        >
          <div className="text-sm font-medium text-orange-600 mb-2">Model 2</div>
          <h2 className="text-2xl font-semibold mb-3">Salary Estimate</h2>
          <p className="text-slate-600 text-sm">
            Given a player&apos;s season stats (age, games, minutes, win shares), predict
            what their salary should be.
          </p>
          <p className="text-xs text-slate-400 mt-4">
            Trained on 12.7k player-seasons from 1990-2017. Median error ~$940k.
          </p>
        </Link>
      </div>
    </div>
  );
}
