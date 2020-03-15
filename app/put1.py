from flask import Flask
import json
import requests
import os.path
from os import path

app = Flask(__name__)


@app.route('/put/<id>', methods=['GET', 'POST', 'PUT'])
def post_json(id):
    # if requests.methods == 'GET':
    #     return "Your methods is wrong"
    # elif requests.methods == 'POST':
    a = path.exists(id)
    if a == 0:
        return "File wasn't existed"
    else:
        data = {"name": "san", "age": 6}
        with open(id, 'w') as f:
            json.dump(data, f)
            f.close()

        # url = '127.0.0.1:5000/post'
        # detail = {"name": "sin", "age": 3}
        # headers = {'Content-type': 'application/json'}
        # reps = requests.post(url, json=detail, headers=headers)
        return "Your file is updated"
