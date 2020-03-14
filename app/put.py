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
    # elif requests.methods == 'PUT':

    a = path.exists(id)
    if a == 0:
        return "File isn't existed"
    else:
        url = '127.0.0.1:5000/put/{0}'.format(id)
        detail = {null}
        headers = {'Content-type': 'application/json'}
        reps = requests.put(url, json=detail, headers=headers)
        return json.dumps(id)


if __name__ == '__main__':
    app.run()
