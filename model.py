# model.py
import pickle

class YourModel:
    def __init__(self, model_path):
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load("/PROJECT/house_value_prediction.pkl")

    def predict(self, input_data):
        return self.model.predict(input_data)
