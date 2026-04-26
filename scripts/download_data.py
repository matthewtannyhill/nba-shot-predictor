import shutil
from pathlib import Path

import kagglehub
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

DEST = Path(__file__).resolve().parent.parent / "data"
DEST.mkdir(exist_ok=True)


def fetch_csv(dataset: str, source_filename: str, dest_name: str) -> Path:
    cache = Path(kagglehub.dataset_download(dataset))
    src = cache / source_filename
    dst = DEST / dest_name
    shutil.copy(src, dst)
    return dst


def fetch_xlsx_as_csv(dataset: str, source_filename: str, dest_name: str) -> Path:
    cache = Path(kagglehub.dataset_download(dataset))
    src = cache / source_filename
    dst = DEST / dest_name
    pd.read_excel(src).to_csv(dst, index=False)
    return dst


shot_logs = fetch_csv(
    "dansbecker/nba-shot-logs", "shot_logs.csv", "shot_logs.csv"
)
seasons = fetch_csv(
    "drgilermo/nba-players-stats", "Seasons_Stats.csv", "seasons_stats.csv"
)
salaries = fetch_xlsx_as_csv(
    "whitefero/nba-player-salary-19902017",
    "Player - Salaries per Year (1990 - 2017).xlsx",
    "salaries.csv",
)

for path in [shot_logs, seasons, salaries]:
    rows = sum(1 for _ in open(path)) - 1
    print(f"{path.name:<25} {path.stat().st_size // 1024:>6} KB  {rows:>7,} rows")
