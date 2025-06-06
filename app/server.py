from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

# Carrega o pipeline completo
model = joblib.load("./modelo_pipeline.pkl")

@app.route("/prever", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Validação de campos
        expected_keys = [
            "Disaster Type", "Start Year", "Total Deaths", "No. Injured",
            "Total Affected", "Total Damage ('000 US$)", "Magnitude", "Country"
        ]

        missing_keys = [key for key in expected_keys if key not in data]
        if missing_keys:
            return jsonify({"error": f"Campos faltando: {', '.join(missing_keys)}"}), 400

        # Cria DataFrame com dados crus, na ordem certa
        input_df = pd.DataFrame([{
            "Disaster Type": data["Disaster Type"],
            "Start Year": data["Start Year"],
            "Total Deaths": data["Total Deaths"],
            "No. Injured": data["No. Injured"],
            "Total Affected": data["Total Affected"],
            "Total Damage ('000 US$)": data["Total Damage ('000 US$)"],
            "Magnitude": data["Magnitude"],
            "Country": data["Country"]
        }])

        # Faz a predição usando o pipeline completo
        prediction = model.predict(input_df)

        return jsonify({"Nivel de Risco": str(prediction[0])})

    except Exception as e:
        return jsonify({"error": f"Ocorreu um erro: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
