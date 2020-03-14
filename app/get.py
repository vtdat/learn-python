from flask import Flask
import json
import requests

app = Flask(__name__)


@app.route('/get/<id>', methods=['GET'])
def get_json(id):
    f = open(id, "r")
    y = json.dumps(f.read())
    return y
