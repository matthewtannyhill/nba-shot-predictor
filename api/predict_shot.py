import json
from http.server import BaseHTTPRequestHandler
from pathlib import Path

import joblib

MODEL_PATH = Path(__file__).parent.parent / "models" / "shot_model.pkl"
_model = joblib.load(MODEL_PATH)

FEATURE_ORDER = ["TOUCH_TIME", "SHOT_CLOCK", "SHOT_DIST", "CLOSE_DEF_DIST", "DRIBBLES"]


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))

        row = [
            float(body["touch_time"]),
            float(body["shot_clock"]),
            float(body["shot_dist"]),
            float(body["close_def_dist"]),
            float(body["dribbles"]),
        ]
        prob = float(_model.predict_proba([row])[0][1])

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"made_probability": prob}).encode())
