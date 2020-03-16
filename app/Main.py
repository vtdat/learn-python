from flask import Flask, request
import json
import os.path
from os import path

app = Flask(__name__)


@app.route('/get/<id>', methods=['GET'])
def get_json(id):
    f = open('/home/sand/Documents/learn-python/app/Data/' + id, "r")
    y = json.dumps(f.read())
    return y


@app.route('/post/<id>', methods=['POST'])
def post_json(id):
    a = path.isfile('/home/sand/Documents/learn-python/app/Data/'+id)
    if a == 1:
        return "File was existed"
    else:
        data = request.data
        with open('/home/sand/Documents/learn-python/app/Data/' + id, 'w') as f:
            json.dump(data, f)
            f.close()
        return "Your file is created"


@app.route('/put/<id>', methods=['PUT'])
def put_json(id):
    a = path.isfile('/home/sand/Documents/learn-python/app/Data/'+id)
    if a == 0:
        return "File wasn't existed"
    else:
        data = request.data
        with open('/home/sand/Documents/learn-python/app/Data/' + id, 'w') as f:
            json.dump(data, f)
            f.close()
        return "Your file is updated"


@app.route('/delete/<id>', methods=['DELETE'])
def delete_json(id):
    a = path.isfile('/home/sand/Documents/learn-python/app/Data/'+id)
    if a == 0:
        return "File isn't existed"
    else:
        os.remove(id)
        return 'File is deleted'


if __name__ == '__main__':
    app.run()

# curl -H "Content-Type: application/json"  -XPOST -d '{"name":"xyz","age":"xyz"}' http://localhost:5000/post/
