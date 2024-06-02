# app.py
from flask import Flask, request, jsonify
from model import YourModel
import os

app = Flask(__name__)

# Initialize the model
model = YourModel('./house_value_prediction.py')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json(force=True)
        
        # Prepare the data for prediction
        input_data = [[
            data['Area'],
            data['No_of_Bedrooms'],
            data['RainWaterHarvesting'],
            data['School'],
            data['ATM'],
            data['ShoppingMall'],
            data['24X7Security'],
            data['PowerBackup'],
            data['CarParking'],
            data['Hospital'],
            data['EncCity']
        ]]
        
        # Make a prediction
        prediction = model.predict(input_data)
        
        # Prepare the response
        output = {'prediction': prediction[0]}
        
        return jsonify(output)
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)
