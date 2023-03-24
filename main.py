from flask import Flask, request
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from logger.log import backend_log
from logger.log import request_log


app = Flask(__name__)
try:
    config_path = Path('./config.cfg')
    load_dotenv(dotenv_path=config_path)
except Exception as error:
    backend_log.error(f"Failed to load configuration file - {error}")
    exit()


@app.route('/api/get-price', method=['GET'])
def get_price():
    prediction = None
    backend_log.info(f"Function 'get_price()' started")
    request_log.info(f"Request was received from <{request.remote_addr}>.")
    try:
        request_data = request.get_json()
        request_log.info(f"Request was sent to the prediction module")

        try:
            prediction = requests.get(url = os.getenv('PREDICTION_URL'), params = request_data)
            request_log.info(f"Response was received from  prediction module")
        
        except Exception as error:
            request_log.error(f"Response was not obtained from the prediction model. Error log - {error}")
    
    except Exception as error:
        backend_log.error(f"Function 'get_price()' failed. Status: {error}")
        request_log.error(f"Request received from <{request.remote_addr}> failed.")
    finally:
        return prediction


if __name__ == '__main__':
    backend_log.info("Start working on the logic module...")
    app.run(debug=False, port=8080)