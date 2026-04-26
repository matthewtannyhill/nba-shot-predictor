import json
import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

ROOT = Path(__file__).resolve().parent.parent
df = pd.read_csv(ROOT / "data" / "shot_logs.csv")

base_features = ["TOUCH_TIME", "SHOT_CLOCK", "SHOT_DIST", "CLOSE_DEF_DIST", "DRIBBLES"]
target = "FGM"

df = df.dropna(subset=base_features + [target, "player_name"])
df = df[df["TOUCH_TIME"] >= 0]

train_df, test_df = train_test_split(
    df, test_size=0.2, random_state=42, stratify=df[target]
)

# Compute player skill from training set only to avoid leakage.
player_skill = train_df.groupby("player_name")[target].mean()
global_mean = float(train_df[target].mean())

train_df = train_df.copy()
test_df = test_df.copy()
train_df["PLAYER_SKILL"] = train_df["player_name"].map(player_skill)
test_df["PLAYER_SKILL"] = test_df["player_name"].map(player_skill).fillna(global_mean)

features = base_features + ["PLAYER_SKILL"]
X_train, y_train = train_df[features], train_df[target].astype(int)
X_test, y_test = test_df[features], test_df[target].astype(int)

model = RandomForestClassifier(
    n_estimators=200, max_depth=12, n_jobs=-1, random_state=42
)
model.fit(X_train, y_train)

preds = model.predict(X_test)
probs = model.predict_proba(X_test)[:, 1]

print(f"Train rows:  {len(X_train):>7,}")
print(f"Test rows:   {len(X_test):>7,}")
print(f"Accuracy:    {accuracy_score(y_test, preds):.3f}")
print(f"AUC:         {roc_auc_score(y_test, probs):.3f}")
print()
print("Feature importance:")
for f, imp in sorted(zip(features, model.feature_importances_), key=lambda x: -x[1]):
    print(f"  {f:<16} {imp:.3f}")
print()
print(classification_report(y_test, preds, target_names=["miss", "made"]))

models_dir = ROOT / "models"
models_dir.mkdir(exist_ok=True)
model_path = models_dir / "shot_model.pkl"
meta_path = models_dir / "shot_model_meta.json"

joblib.dump(model, model_path)
with open(meta_path, "w") as f:
    json.dump(
        {
            "feature_order": features,
            "global_mean": global_mean,
            "player_skill": player_skill.to_dict(),
        },
        f,
        indent=2,
    )

print(f"Saved {model_path} ({model_path.stat().st_size // 1024} KB)")
print(f"Saved {meta_path} ({meta_path.stat().st_size // 1024} KB, {len(player_skill)} players)")
