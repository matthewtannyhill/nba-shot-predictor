"use client";

import { useState } from "react";

type Result = { made_probability: number };

export default function ShotPage() {
  const [form, setForm] = useState({
    shot_clock: "12",
    touch_time: "2.5",
    shot_dist: "15",
    close_def_dist: "4",
    dribbles: "2",
  });
  const [result, setResult] = useState<Result | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const res = await fetch("/api/predict_shot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      setResult(await res.json());
    } catch (err) {
      setError(err instanceof Error ? err.message : "Request failed");
    } finally {
      setLoading(false);
    }
  }

  function update(key: keyof typeof form, value: string) {
    setForm((f) => ({ ...f, [key]: value }));
  }

  return (
    <div className="max-w-2xl mx-auto px-6 py-12">
      <h1 className="text-3xl font-bold mb-2">Shot Outcome</h1>
      <p className="text-slate-600 mb-8">
        Predicts the probability a shot goes in, given pre-shot tracking features.
      </p>

      <form onSubmit={handleSubmit} className="space-y-4 bg-white p-6 rounded-xl border border-slate-200">
        <Field label="Shot clock (sec)" value={form.shot_clock} onChange={(v) => update("shot_clock", v)} />
        <Field label="Touch time (sec)" value={form.touch_time} onChange={(v) => update("touch_time", v)} />
        <Field label="Shot distance (ft)" value={form.shot_dist} onChange={(v) => update("shot_dist", v)} />
        <Field label="Closest defender distance (ft)" value={form.close_def_dist} onChange={(v) => update("close_def_dist", v)} />
        <Field label="Dribbles" value={form.dribbles} onChange={(v) => update("dribbles", v)} />

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-orange-500 hover:bg-orange-600 disabled:bg-slate-300 text-white font-medium py-2 px-4 rounded-lg transition"
        >
          {loading ? "Predicting…" : "Predict"}
        </button>
      </form>

      {error && (
        <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-800 text-sm">
          {error}
        </div>
      )}

      {result && (
        <div className="mt-6 p-6 bg-white border border-slate-200 rounded-xl text-center">
          <div className="text-sm text-slate-500 mb-1">Probability shot goes in</div>
          <div className="text-5xl font-bold text-orange-600">
            {(result.made_probability * 100).toFixed(1)}%
          </div>
        </div>
      )}
    </div>
  );
}

function Field({
  label,
  value,
  onChange,
}: {
  label: string;
  value: string;
  onChange: (v: string) => void;
}) {
  return (
    <label className="block">
      <span className="block text-sm font-medium text-slate-700 mb-1">{label}</span>
      <input
        type="number"
        step="any"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-orange-400 focus:border-orange-400 outline-none"
        required
      />
    </label>
  );
}
