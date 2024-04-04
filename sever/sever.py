from flask import Flask, request
import base64
from pyngrok import ngrok
import webbrowser

app = Flask(__name__)

ngrok.set_auth_token("2dSuZ0eOuPERzfCOYAxya3k9Jvg_4QMe3M7CqAaTfi2tA8Soo")
public_url = ngrok.connect(5000).public_url
@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        # Get image data from request
        data = request.json
        image_data = data['image']
        
        # Decode Base64 image data
        image_bytes = base64.b64decode(image_data)
        
        # Save the image to a file (optional)
        with open('received_image.jpg', 'wb') as f:
            f.write(image_bytes)
        
        # You can process the image data here as needed
        
        return "Image received successfully", 200

    except Exception as e:
        print("Error:", e)
        return "Error processing image", 500

if __name__ == '__main__':
    print(public_url)
    webbrowser.open_new('http://127.0.0.1.5000/')
    app.run()
