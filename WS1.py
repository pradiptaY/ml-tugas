from flask import Flask, jsonify, request
from flasgger import Swagger
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)
Swagger(app)

@app.route('/predict/task', methods = ['POST'])
def predict():
    """
        ini adalah Endpoint untuk menginput data task.
        ---
        tags:
            - Rest Controller
        parameter:
            - name: body
                in: body
                required: true
                schema:
                    id: product
                    required:
                    - calories
                    - protein
                    - fat
                    - sodium
                    - fiber
                    - carbo
                    - potass
                    - vitamins
                properties:
                    calories:
                        type: int
                        description: input with valid data
                        default: 0
                    protein:
                        type: int
                        description: input with valid data
                        default: 0
                    fat:
                        type: int
                        description: input with valid data
                        default: 0
                    sodium:
                        type: int
                        description: input with valid data
                        default: 0
                    fiber:
                        type: int
                        description: input with valid data
                        default: 0
                    carbo:
                        type: int
                        description: input with valid data
                        default: 0
                    potass:
                        type: int
                        description: input with valid data
                        default: 0
                    vitamins:
                        type: int
                        description: input with valid data
                        default: 0
        responses:
            200:
                description: Success Input
        """
    new_task = request.get_json()

    calories = new_task['calories']
    protein = new_task['protein']
    fat = new_task['fat']
    sodium = new_task['sodium']
    fiber = new_task['fiber']
    carbo = new_task['carbo']
    potass = new_task['potass']
    vitamins = new_task['vitamins']

    X_New = np.array([[calories,  protein,  fat,  sodium,  fiber,  carbo,  potass,  vitamins]])

    clf = joblib.load('static/cerealRegressor.pkl')

    resultPredict = clf[0].predict(X_New)


    return jsonify({'message': format(clf[1].target_names[resultPredict])})