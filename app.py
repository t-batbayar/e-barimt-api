from ctypes import c_char_p
from ctypes import *
import json
from sys import platform
import flask
from flask import request, jsonify
import logging

app = flask.Flask(__name__)
app.config['DEBUG'] = True

def formatResult(result):
    try:
        result.restype = c_char_p
        response = result().decode('utf-8')
        print('RESPONSE', response)
        data = response.replace("\n", "")
        data = response.replace("\\\"", "'")
        data = data.replace("\\", "")
        data = json.loads(data)
        return data
    except Exception as e: 
        logging.exception('formatResult error: ', result)

@app.route('/', methods=['GET'])
def home():
    data = {
        'data': 'Hello World!'
    }
    return jsonify(data)

@app.route('/check-api', methods=['GET'])
def check_api():
    try:
        bridge = CDLL('./libPosAPI.so')
        result = bridge.checkApi
        data = formatResult(result)

        return jsonify(data)
    except Exception as e: 
        logging.exception('formatResult error: ', result)

@app.route('/get-information', methods=['GET'])
def get_information():
    try:
        bridge = CDLL('./libPosAPI.so')
        result = bridge.getInformation
        data = formatResult(result)
        return jsonify(data)
    except Exception as e: 
        logging.exception('formatResult error: ', result)

@app.route('/put', methods=['POST'])
def put():
    try: 
        request_body = request.get_json()
        bridge = CDLL('./libPosAPI.so')
        result = bridge.put
        result.restype = c_char_p
        body = json.dumps(request_body)
        body = body.encode('utf-8')
        response = result(body).decode('utf-8')
        data = response.replace("\n", "")
        data = data.replace("\\", "")
        data = json.loads(data)
        return jsonify(data)
    except Exception as e:
        logging.exception('formatResult error: ', result)

@app.route('/send-data', methods=['GET'])
def send_data():
    try:
        bridge = CDLL('./libPosAPI.so')
        result = bridge.sendData
        data = formatResult(result)
        return jsonify(data)
    except Exception as e:
        logging.exception('formatResult error: ', result)

app.run(host="0.0.0.0")
