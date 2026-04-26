import json
import math
from http.server import BaseHTTPRequestHandler
from pathlib import Path

import joblib

MODEL_PATH = Path(__file__).parent.parent / "models" / "agent_model.pkl"
_model = joblib.load(MODEL_PATH)

FEATURE_ORDER = ["Age", "G", "MP", "OWS", "DWS", "WS"]


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))

        row = [
            float(body["age"]),
            float(body["games"]),
            float(body["minutes"]),
            float(body["ows"]),
            float(body["dws"]),
            float(body["ws"]),
        ]
        log_salary = float(_model.predict([row])[0])
        salary = math.expm1(log_salary)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"predicted_salary": salary}).encode())
