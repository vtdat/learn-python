from flask import Flask
import json
import requests
import os.path
from os import path

app = Flask(__name__)


@app.route('/post/<id>', methods=['GET', 'POST'])
def post_json(id):
    # if requests.methods == 'GET':
    #     return "Your methods is wrong"
    # elif requests.methods == 'POST':

    a = path.exists(id)
    if a == 1:
        return "File was existed"
    else:
        url = '127.0.0.1:5000/post'
        detail = {"name": "sin", "age": 3}
        headers = {'Content-type': 'application/json'}
        reps = requests.post(url, json=detail, headers=headers)
        return json.dumps(id)


if __name__ == '__main__':
    app.run()
