from flask import Flask, request
import requests
import os
from dotenv import load_dotenv
from pathlib import Path


app = Flask(__name__)
config_path = Path('./config.cfg')
load_dotenv(dotenv_path=config_path)


@app.route('/api/get-price', method=['GET'])
def get_price():
    request_data = request.get_json()
    prediction = requests.get(url = os.getenv('PREDICTION_URL'), params = request_data)
    return prediction


if __name__ == '__main__':
    app.run(debug=False, port=8080)