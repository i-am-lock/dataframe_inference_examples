import pickle
from flask import Flask, jsonify, request
import pandas as pd


app = Flask(__name__)


with open('artifacts/mapper.pkl', 'rb') as handle:
    mapper = pickle.load(handle)

with open('artifacts/model.pkl', 'rb') as handle:
    model = pickle.load(handle)


def predict(self, json_dict):
    test_data = pd.DataFrame(json_dict)
    features = self.features_pipe.transform(test_data)
    return self.model.predict(features)

@app.route('/model/predict', methods=["POST"])
def main():
    input_data = request.get_json(request.data)
    input_data_frame = pd.DataFrame([input_data])
    features = mapper.transform(input_data_frame)
    predict = model.predict(features)
    return jsonify({"ans": int(predict[0])})
    
if __name__ == "__main__":
    app.run()
    
#####
#  curl -X post 127.0.0.1:5000/model/predict -d '{"PassengerId": 2, "Survived": 1, "Pclass": 1, "Name": "Cumings, Mrs. John Bradley (Florence Briggs Thayer)", "Sex": "female", "Age": 38.0, "SibSp": 1, "Parch": 0, "Ticket": "PC 17599", "Fare": 71.2833, "Cabin": "C85", "Embarked": "C"}'  -H "Content-Type: application/json"
#####
