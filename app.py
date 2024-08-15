from flask import Flask, request, render_template  # Add missing imports
import pickle
import numpy as np

app = Flask(__name__)

with open('model1.0.sav', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        features = [
            float(request.form['u_q']),
            float(request.form['coolant']),
            float(request.form['stator_winding']),
            float(request.form['u_d']),
            float(request.form['stator_tooth']),
            float(request.form['motor_speed']),
            float(request.form['i_d']),
            float(request.form['i_q']),
            float(request.form['stator_yoke']),
            float(request.form['ambient']),
            float(request.form['torque'])
        ]

        prediction = model.predict([features])[0]

        return f'Predicted Permanent Magnet Temperature: {prediction:.2f}'
    except KeyError as e:
        return f'Missing form field: {str(e)}', 400
    except Exception as e:  # Fixed the typo here
        return f'An error occurred: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=False)
