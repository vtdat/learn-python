from flask import Flask
import json
import requests
import os.path
from os import path

app = Flask(__name__)


@app.route('/delete/<id>', methods=['GET', 'DELETE'])
def post_json(id):
    # if requests.methods == 'GET':
    #     return "Your methods is wrong"
    # elif requests.methods == 'POST':

    a = path.exists(id)
    if a == 0:
        return "File isn't existed"
    else:
        del id
        return 'Done'


if __name__ == '__main__':
    app.run()
