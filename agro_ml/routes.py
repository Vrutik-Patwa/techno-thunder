from flask import render_template,request
from agro_ml import app
import requests
import pickle
import base64
import numpy as np
from flask import jsonify
from flask_cors import CORS
CORS(app)
# with open('fruit_quality_prediction.pkl', 'rb') as file:
#     model_fruit = pickle.load(file)
def process_fruit(data):
    processed_data = np.array(data).reshape(1, -1)
    
    # Pass the processed data through your model
    prediction = model_fruit.predict(processed_data)
    
    # Return the processed data and prediction as a response
    return jsonify({'processed_data': processed_data.tolist(), 'prediction': prediction.tolist()})

with open('crop_prediction.pkl','rb') as f:
        model_crop = pickle.load(f)
def process_crop(data):
    processed_data = np.array(data).reshape(1, -1)
    # print(processed_data)
    # Pass the processed data through your model
    prediction = model_crop.predict(processed_data)
    
    # Return the processed data and prediction as a response
    return jsonify({'processed_data':        processed_data.tolist(), 'prediction': prediction.tolist()})
@app.route('/')
@app.route('/locust_prevention')


def locust_prevention():
    

    return render_template('locust.html')


@app.route('/leaf_detection')
def leaf_detection():
    return render_template('leaf.html')

@app.route('/fruit_quality')
def fruit_detection():
    if request.method == 'POST':
        data = request.json 
        

        return process_fruit(data)



@app.route('/crop_prediction',methods=['GET','POST'])
def crop_prediction():
    if request.method == 'POST':
        data = request.json
        data = list(data.values())
        data =[data]
        return process_crop(data)
    
    return render_template("crop.html")
# Set a threshold for the minimum size of the received data
MIN_IMAGE_SIZE = 1000  # Adjust this value based on your requirements
i=0
@app.route('/upload', methods=['GET','POST'])
def upload_image():
    try:
        # Get raw data from request
        raw_data = request.get_data()
        
        # Print the length of the received data
        data_length = len(raw_data)
        print("Received data length:", data_length)
        
        # Check if the data size is below the minimum threshold
        if data_length < MIN_IMAGE_SIZE:
            return "Invalid data received", 400
        
        # Decode Base64 image data
        image_bytes = base64.b64decode(raw_data)
        
        # Save the image to a file (optional)
        with open('received_image.jpg', 'wb') as f:
            f.write(image_bytes)
        
        # You can process the image data here as needed
        
        return "Image received successfully", 200

    except Exception as e:
        print("Error:", e)
        return "Error processing image", 500
    
    return render_template('image.html',image = image_bytes)

@app.route('/send_data', methods=['GET','POST'])
def send_data_to_node():
    global value
    value = value.tolist()
    data = {{'output': value},{}}  # Data you want to send
    response = requests.post('https://technothunder-unplugged1-0-hardwarehack.onrender.com/api/ideal-crop', json=data)
    return response.text


@app.route("/recv",methods=['GET','POST'])
def data():
    if request.method == 'POST':
        data = request.json
      
        
        # Do whatever you want with the received data
        print(f"Received data:{data}")
        
        # You can also store the data in a database or perform other operations
        
        return "Data received successfully", 200
    else:
        return "Method not allowed", 405
if __name__ == '__main__':
    app.run()

    
   