from flask import Flask
import json

app = Flask(__name__)


@app.route('/get')
def get_json():
    f = open("a.json", "r")
    y = json.dumps(f.read())
    return y
