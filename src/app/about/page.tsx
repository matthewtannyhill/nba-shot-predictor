export default function AboutPage() {
  return (
    <div className="max-w-2xl mx-auto px-6 py-12 prose prose-slate">
      <h1 className="text-3xl font-bold mb-6">About</h1>

      <h2 className="text-xl font-semibold mt-8 mb-3">History</h2>
      <p className="mb-4">
        Originally built as a 2019 BYU class project. The web app is Django and the
        prediction backend was Azure ML Studio (classic), retired by Microsoft on
        August 31, 2024.
      </p>
      <p className="mb-4">
        Rebuilt in 2026 with two scikit-learn models trained locally, a Next.js
        frontend, and Python serverless functions on Vercel. The original repo is
        archived at <a className="text-orange-600 hover:underline" href="https://github.com/matthewtannyhill/nbashots">github.com/matthewtannyhill/nbashots</a>.
      </p>

      <h2 className="text-xl font-semibold mt-8 mb-3">Models</h2>
      <p className="mb-4">
        <strong>Shot model:</strong> Random Forest classifier trained on the Kaggle
        NBA Shot Logs 2014-15 dataset (128k shots). Features: shot clock, touch time,
        shot distance, closest defender distance, dribbles. Test AUC 0.634, accuracy
        61.9%. Roughly the published ceiling on this feature set.
      </p>
      <p className="mb-4">
        <strong>Salary model:</strong> Random Forest regressor trained on a join of
        Basketball-Reference season stats and NBA salaries (1990-2017, 12.7k
        player-seasons). Predicts log(Salary) from age, games, minutes, and win share
        components. Median absolute error ~$940k. Salaries are not adjusted for
        salary-cap inflation.
      </p>

      <h2 className="text-xl font-semibold mt-8 mb-3">Honest caveats</h2>
      <ul className="list-disc list-inside space-y-1 text-slate-700">
        <li>Shot model predicts &quot;miss&quot; more often than &quot;make&quot; because misses are ~54% of training data.</li>
        <li>Salary model treats 1995 dollars and 2017 dollars the same, which they aren&apos;t.</li>
        <li>Neither model captures defensive scheme, fatigue, contract year, or team budget.</li>
      </ul>
    </div>
  );
}
