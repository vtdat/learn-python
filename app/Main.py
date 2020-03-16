from flask import Flask, request
import json
import os.path
from os import path

app = Flask(__name__)


@app.route('/get/<id>', methods=['GET'])
def get_json(id):
    track = os.path.join(app.root_path, 'Data', id)
    f = open(track, "r")
    return  f.read()


@app.route('/post/<id>', methods=['POST'])
def post_json(id):
    track = os.path.join(app.root_path, 'Data', id)
    a = path.isfile(track)
    if a == 1:
        return "File was existed"
    else:
        data = request.data
        with open(track, 'w') as f:
            json.dump(data, f)
            f.close()
        return "Your file is created"


@app.route('/put/<id>', methods=['PUT'])
def put_json(id):
    track = os.path.join(app.root_path, 'Data', id)
    a = path.isfile(track)
    if a == 0:
        return "File wasn't existed"
    else:
        data = request.data
        with open(track, 'w') as f:
            json.dump(data, f)
            f.close()
        return "Your file is updated"


@app.route('/delete/<id>', methods=['DELETE'])
def delete_json(id):
    track = os.path.join(app.root_path, 'Data', id)
    a = path.isfile(track)
    if a == 0:
        return "File isn't existed"
    else:
        os.remove(track)
        return 'File is deleted'


if __name__ == '__main__':
    app.run()

# curl -H "Content-Type: application/json"  -XPOST -d '{"name":"xyz","age":"xyz"}' http://localhost:5000/post/

