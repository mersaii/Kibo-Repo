from flask import jsonify, Flask, request
import joblib
import numpy as np
import sklearn

app = Flask(__name__)

model = joblib.load("music_genre_model.pkl")

@app.route('/', methods=['GET'])
def home():
    return jsonify({'service':'available'})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    features = np.array([
        float(data['acousticness']),
        float(data['danceability']),
        float(data['duration_ms']),
        float(data['energy']),
        float(data['instrumentalness']),
        float(data['key']),
        float(data['liveness']),
        float(data['loudness']),
        float(data['speechiness']),
        float(data['tempo']),
        float(data['mode']),
        float(data['valence']),     
    ]).reshape(1,-1)


    prediction = model.predict(features)
    answer = ''
    print(prediction)

    if prediction == 4:
        answer = 'Rock'
    elif prediction == 3:
        answer = 'Rap'
    elif prediction == 1:
        answer = 'Country'
    elif prediction == 0:
        answer = 'Classical'
    elif prediction == 2:
        answer = 'EDM'
    else:
        answer ='error'

    print({'predicted_genre': answer})
    return jsonify({'Genre': answer, 'status_code':200})

if __name__ == '__main__':
    app.run()