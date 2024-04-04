import pickle
import numpy as np
from flask import jsonify
data = {'temp': 45, 'humid': 45, 'rainfall': 100}

# Extract values from the dictionary
values = list(data.values())

# Create a 2D array with all values in a single inner list
two_d_array = [values]

print(two_d_array)

with open('crop_prediction.pkl','rb') as f:
        model_crop = pickle.load(f)
def process_crop(data):
    processed_data = np.array(data).reshape(1, -1)
    # print(processed_data)
    # Pass the processed data through your model
    prediction = model_crop.predict(processed_data)
    
    # Return the processed data and prediction as a response
    return ({'processed_data': processed_data.tolist(), 'prediction': prediction.tolist()})

print(process_crop(two_d_array))