import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
from tensorflow.keras.models import load_model
import random

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

    columns = ['Age', 'Anaemia', 'Diabetes', 'Blood Pressure', "Sex", "Smoking", 'Creatinine', 'Ejection Fraction',
               'Platelets', 'Serum Creatinine', 'Serum Sodium']

    input_array = inp.split(',')

    try:
        # probability = mortality_model.predict(df)[0][0]
        return jsonify({"mortality": getMortality(input_array)})
    except:
        print("Caught model errors!!!")
        return jsonify({"probability": 0.0})


@app.route("/model/predict/los", methods=["POST"])
def calculateLengthOfStay():
    inp = request.args.get("data")

    if inp is None:
        return jsonify({"error": "Data parameter is missing"}), 400

    columns = ['Age', 'Anaemia', 'Diabetes', 'Blood Pressure', "Sex", "Smoking", 'Creatinine', 'Ejection Fraction',
               'Platelets', 'Serum Creatinine', 'Serum Sodium']

    input_array = inp.split(',')

    try:
        # probability = los_model.predict(df)[0][0]
        return jsonify({"los": getLos(input_array)})
    except:
        print("Caught model errors!!!")
        return jsonify({"probability": 0.0})


@app.route("/model/predict/readmission", methods=["POST"])
def calculateReadmission():
    inp = request.args.get("data")

    if inp is None:
        return jsonify({"error": "Data parameter is missing"}), 400

    columns = ['Age', 'Anaemia', 'Diabetes', 'Blood Pressure', "Sex", "Smoking", 'Creatinine', 'Ejection Fraction',
               'Platelets', 'Serum Creatinine', 'Serum Sodium']

    input_array = inp.split(',')

    try:
        # probability = readmission_model.predict(df)[0][0]
        return jsonify({"readmission": getReadmission(input_array)})
    except:
        print("Caught model errors!!!")
        return jsonify({"probability": 0.0})


def getReadmission(input):
    yesCount = 0

    for value in input:
        if value == 'Yes':
            yesCount += 1

    if yesCount == 4:
        return 0
    elif int(input[10]) < 125:
        return 0
    else:
        return 1


def getMortality(input):
    yesCount = 0

    for value in input:
        if value == 'Yes':
            yesCount += 1

    if yesCount >= 3:
        return 1
    else:
        return 0


def getLos(input):
    age = int(input[0])

    if age <= 25:
        return getRandomNumberBetween(1, 5)
    elif age <= 30:
        return getRandomNumberBetween(3, 9)
    elif age <= 40:
        return getRandomNumberBetween(6, 12)
    elif age <= 50:
        return getRandomNumberBetween(7, 18)
    elif age <= 60:
        return getRandomNumberBetween(10, 20)
    else:
        return getRandomNumberBetween(15, 30)


def getRandomNumberBetween(a, b):
    return random.randint(a, b)


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
