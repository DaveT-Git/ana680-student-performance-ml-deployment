from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model (must be in the same folder as app.py)
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("Error: model.pkl not found in the project root folder!")
    raise

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', values={}, prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from the form
        math    = float(request.form['math_score'])
        reading = float(request.form['reading_score'])
        writing = float(request.form['writing_score'])
    except (KeyError, ValueError):
        return "Invalid input. Please enter valid numbers for all scores.", 400

    # Prepare input array (must match the order used during training)
    features = np.array([[math, reading, writing]])

    # Make prediction
    prediction = model.predict(features)[0]  # e.g. 'group C'

    # Keep the entered values so the form stays filled
    values = {
        'math_score':    math,
        'reading_score': reading,
        'writing_score': writing
    }

    return render_template('index.html',
                          values=values,
                          prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
