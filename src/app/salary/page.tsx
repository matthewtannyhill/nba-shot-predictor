"use client";

import { useState } from "react";

type Result = { predicted_salary: number };

export default function SalaryPage() {
  const [form, setForm] = useState({
    age: "26",
    games: "75",
    minutes: "2200",
    ows: "4.5",
    dws: "2.0",
    ws: "6.5",
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
      const res = await fetch("/api/predict_salary", {
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
      <h1 className="text-3xl font-bold mb-2">Salary Estimate</h1>
      <p className="text-slate-600 mb-8">
        Predicts an NBA salary from a single season&apos;s box-score stats. Trained on
        1990-2017 data (not inflation-adjusted).
      </p>

      <form onSubmit={handleSubmit} className="space-y-4 bg-white p-6 rounded-xl border border-slate-200">
        <Field label="Age" value={form.age} onChange={(v) => update("age", v)} />
        <Field label="Games played" value={form.games} onChange={(v) => update("games", v)} />
        <Field label="Minutes played (season total)" value={form.minutes} onChange={(v) => update("minutes", v)} />
        <Field label="Offensive Win Shares (OWS)" value={form.ows} onChange={(v) => update("ows", v)} />
        <Field label="Defensive Win Shares (DWS)" value={form.dws} onChange={(v) => update("dws", v)} />
        <Field label="Total Win Shares (WS)" value={form.ws} onChange={(v) => update("ws", v)} />

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
          <div className="text-sm text-slate-500 mb-1">Predicted salary</div>
          <div className="text-5xl font-bold text-orange-600">
            ${result.predicted_salary.toLocaleString("en-US", { maximumFractionDigits: 0 })}
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
