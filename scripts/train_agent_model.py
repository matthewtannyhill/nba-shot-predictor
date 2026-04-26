import json
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

stats = pd.read_csv(DATA / "seasons_stats.csv")
salary = pd.read_csv(DATA / "salaries.csv")

salary = salary.rename(columns={"Player Name": "Player", "Salary in $": "Salary"})
salary["Year"] = salary["Season End"].astype("Int64")
df = stats.merge(salary[["Player", "Year", "Salary"]], on=["Player", "Year"], how="inner")

features = ["Age", "G", "MP", "OWS", "DWS", "WS"]
target = "Salary"

df = df.dropna(subset=features + [target])
df = df[df[target] > 0]
df["log_salary"] = np.log1p(df[target])

X = df[features]
y = df["log_salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(
    n_estimators=200, max_depth=12, n_jobs=-1, random_state=42
)
model.fit(X_train, y_train)

preds_log = model.predict(X_test)
preds = np.expm1(preds_log)
actual = np.expm1(y_test)

print(f"Joined rows: {len(df):>7,}")
print(f"Train rows:  {len(X_train):>7,}")
print(f"Test rows:   {len(X_test):>7,}")
print(f"R² (log):    {r2_score(y_test, preds_log):.3f}")
print(f"R² (raw):    {r2_score(actual, preds):.3f}")
print(f"MAE:         ${mean_absolute_error(actual, preds):>12,.0f}")
print(f"Median err:  ${np.median(np.abs(actual - preds)):>12,.0f}")
print()
print("Feature importance:")
for f, imp in sorted(zip(features, model.feature_importances_), key=lambda x: -x[1]):
    print(f"  {f:<6} {imp:.3f}")

models_dir = ROOT / "models"
models_dir.mkdir(exist_ok=True)
model_path = models_dir / "agent_model.pkl"
meta_path = models_dir / "agent_model_meta.json"

joblib.dump(model, model_path)
with open(meta_path, "w") as f:
    json.dump(
        {
            "feature_order": features,
            "target": "log1p(Salary in USD)",
            "training_years": [int(df["Year"].min()), int(df["Year"].max())],
        },
        f,
        indent=2,
    )

print(f"Saved {model_path} ({model_path.stat().st_size // 1024} KB)")
print(f"Saved {meta_path}")
