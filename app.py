from flask import Flask, request
from flask_restful import Resource, Api
from predictingManager import PredictingManager

app = Flask(__name__)
api = Api(app)

class Titanic(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        predictingManager = PredictingManager()
        predict_data = predictingManager.do_predict(data)
        return {'passengerId':data['passengerId'],'name' : data['name'],'survived':predict_data[0], 'survival_probability':predict_data[1]}

api.add_resource(Titanic, '/titanic/predict')
app.run(host = '0.0.0.0',port=5000,debug=True)