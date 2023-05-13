from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
import pickle

app = Flask(__name__)

# Set the decision threshold
decision_threshold = 0.9

# Set the path to the saved model
model_path = "svm_model.pkl"

# Load the saved model from disk
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Define a function to preprocess the image
def preprocess_image(image):
    # Resize the image to 100x100
    image = cv2.resize(image, (100, 100))
    # Flatten the resized image to a 1D array
    flattened_image = image.reshape(1, -1)
    return flattened_image

# Define the route for the predict page
@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the request
    image = request.files['image'].read()
    # Decode the image using OpenCV
    image = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    # Preprocess the image
    preprocessed_image = preprocess_image(image)
    # Use the trained model to make a prediction
    predicted_probabilities = model.predict_proba(preprocessed_image)
    if max(predicted_probabilities[0]) >= decision_threshold:
        predicted_name = model.classes_[np.argmax(predicted_probabilities)]
        predicted_probability = max(predicted_probabilities[0])
        # Check if the confidence level is 90% or above
        if predicted_probability >= 0.9:
            return '<label>The predicted author is {} with an accuracy of {:.2f}%</label>'.format(predicted_name, predicted_probability*100)
    else:
        predicted_probability = max(predicted_probabilities[0])
        return '<label>Unknown. <br> Insufficient accuracy of {:.2f}% to predict.</label>'.format(predicted_probability*100)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('home.html')


# Define the route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# Define the route for the prediction page
@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True)
