from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import os
import datetime
import joblib

# -----------------------------
# Path Configuration
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_FOLDER = os.path.join(BASE_DIR, "..", "frontend")

MODEL_PATH = os.path.join(BASE_DIR, "model", "disease_model.pkl")

# -----------------------------
# Flask App Setup
# -----------------------------
app = Flask(
    __name__,
    static_folder=FRONTEND_FOLDER,
    static_url_path=""
)

CORS(app)

# -----------------------------
# Load ML Model
# -----------------------------
model = joblib.load(MODEL_PATH)

# -----------------------------
# Routes - HTML Pages
# -----------------------------
@app.route("/")
def login():
    return send_from_directory(FRONTEND_FOLDER, "login.html")


@app.route("/admin")
def admin():
    return send_from_directory(FRONTEND_FOLDER, "admin.html")


@app.route("/patient")
def patient():
    return send_from_directory(FRONTEND_FOLDER, "patient.html")


@app.route("/history")
def history():
    return send_from_directory(FRONTEND_FOLDER, "history.html")


# -----------------------------
# Static Files
# -----------------------------
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(FRONTEND_FOLDER, path)


# -----------------------------
# Prediction API (ML Based)
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        name = data.get("name", "").strip()
        age = float(data.get("age", 0))
        height = float(data.get("height", 0))
        weight = float(data.get("weight", 0))
        hr = float(data.get("hr", 0))
        glucose = float(data.get("glucose", 0))

        # BMI Calculation
        bmi = 0
        if height > 0:
            bmi = weight / ((height / 100) ** 2)

        # ML Model Prediction
        # model trained with: age, blood_pressure, glucose, heart_rate
        prediction = model.predict([[age,120,glucose,hr]])

        disease = prediction[0]

        # Risk Score
        risk_score = 0

        if glucose > 180:
            risk_score += 30
        if hr > 110:
            risk_score += 25
        if bmi > 30:
            risk_score += 20
        if age > 60:
            risk_score += 15

        # Risk Level
        if risk_score >= 60:
            risk_level = "High"
        elif risk_score >= 30:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        return jsonify({

            "name": name,
            "date": str(datetime.date.today()),
            "bmi": round(bmi, 2),
            "risk_score": risk_score,
            "risk_level": risk_level,
            "disease": disease

        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 400


# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)