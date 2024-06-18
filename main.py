import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

los_model = load_model("models/LOS_model.h5")
mortality_model = load_model("models/Mortality_model.h5")
readmission_model = load_model("models/Readmission_model.h5")


@app.route("/")
def index():
    return "Welcome to Heart Attack Predictor ML Models service!!!"


@app.route("/model/predict/mortality", methods=["POST"])
def calculateMortality():
    inp = request.args.get("data")

    if inp is None:
        return jsonify({"error": "Data parameter is missing"}), 400

    inp = [int(float(num)) if float(num).is_integer() else float(num) for num in inp.split(',')]

    columns = ['Age', 'Anaemia', 'Diabetes', 'Bloob Pressure', "Sex", "Smoking", 'Creatinine', 'Ejection Fraction',
               'Platelets', 'Serum Creatinine', 'Serum Sodium']
    df = pd.DataFrame([inp], columns=columns)

    try:
        # probability = mortality_model.predict(df)[0][0]
        return jsonify({"mortality": 5})
    except:
        print("Caught model errors!!!")
        return jsonify({"probability": 0.0})


@app.route("/model/predict/los", methods=["POST"])
def calculateLengthOfStay():
    inp = request.args.get("data")

    if inp is None:
        return jsonify({"error": "Data parameter is missing"}), 400

    inp = [int(float(num)) if float(num).is_integer() else float(num) for num in inp.split(',')]

    columns = ['Age', 'Anaemia', 'Diabetes', 'Bloob Pressure', "Sex", "Smoking", 'Creatinine', 'Ejection Fraction',
               'Platelets', 'Serum Creatinine', 'Serum Sodium']
    df = pd.DataFrame([inp], columns=columns)

    try:
        # probability = los_model.predict(df)[0][0]
        return jsonify({"length_of_stay": 1})
    except:
        print("Caught model errors!!!")
        return jsonify({"probability": 0.0})


@app.route("/model/predict/readmission", methods=["POST"])
def calculateReadmission():
    inp = request.args.get("data")

    if inp is None:
        return jsonify({"error": "Data parameter is missing"}), 400

    inp = [int(float(num)) if float(num).is_integer() else float(num) for num in inp.split(',')]

    columns = ['Age', 'Anaemia', 'Diabetes', 'Bloob Pressure', "Sex", "Smoking", 'Creatinine', 'Ejection Fraction',
               'Platelets', 'Serum Creatinine', 'Serum Sodium']
    df = pd.DataFrame([inp], columns=columns)

    try:
        # probability = readmission_model.predict(df)[0][0]
        return jsonify({"readmission": 0})
    except:
        print("Caught model errors!!!")
        return jsonify({"probability": 0.0})


# TODO: Comment this when running the main
# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=False, port=8081, host='0.0.0.0')

# TODO: Comment this when running flask
# if __name__ == "__main__":
#     inp = [27, 0, 3, 0, 0, 0, 1, 3, 3, 3, 60]
#
#     columns = ['Age', 'Anaemia', 'Diabetes', 'Bloob Pressure', "Sex", "Smoking", 'Creatinine', 'Ejection Fraction',
#                'Platelets', 'Serum Creatinine', 'Serum Sodium']
#     df = pd.DataFrame([inp], columns=columns)
#     print(1)
