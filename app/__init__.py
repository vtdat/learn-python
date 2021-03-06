from flask import Flask
from flask import request
import os
import json

app = Flask(__name__)
app.url_map.strict_slashes=True


@app.route('/json/')
def index():
  return json.dumps(os.listdir(os.path.join(app.root_path, 'data')))


@app.route('/json/<string:filename>', methods=['GET'])
def get(filename):
  msg = ""
  path = os.path.join(app.root_path, 'data', filename)
  try:
    file = open(path, 'r')
  except FileNotFoundError as err:
    print("{0}".format(err))
    msg = "File not found!"
  else:
    try:
      msg = json.load(file)
    finally:
      file.close()
  return msg


@app.route('/json/<string:filename>', methods=['DELETE'])
def delete(filename):
  msg = ""
  path = os.path.join(app.root_path, 'data', filename)
  if not os.path.isfile(path):
    msg = "File not found!"
  else:
    try:
      os.remove(path)
      msg = "OK"
    except Exception as err:
      print("{0}".format(err))
      msg = "Something went wrong!"
  return msg


@app.route('/json/<string:filename>', methods=['POST'])
def post(filename):
  msg = ""
  path = os.path.join(app.root_path, 'data', filename)
  if os.path.isfile(path):
    msg = "File exists!"
  else:
    try:
      file = open(path, 'w')
    except Exception as err:
      msg = "Something went wrong!"
      print("{0}".format(err))
    else:
      try:
        if file.write(json.dumps(request.json, indent=2)) == 0:
          msg = "Data should not be empty"
        else:
          msg = "OK"
      except Exception as err:
        msg = "Something went wrong!"
        print("{0}".format(err))
        os.remove(path)
      finally:
        file.close()
  return msg


@app.route('/json/<string:filename>', methods=['PUT'])
def put(filename):
  msg = ""
  path = os.path.join(app.root_path, 'data', filename)
  if not os.path.isfile(path):
    msg = "File not exists!"
  else:
    try:
      file = open(path, 'w')
    except Exception as err:
      msg = "Something went wrong!"
      print("{0}".format(err))
    else:
      try:
        if file.write(json.dumps(request.json, indent=2)) == 0:
          msg = "Data should not be empty"
        else:
          msg = "OK"
      except Exception as err:
        print("{0}".format(err))
        msg = "Something went wrong!"
      finally:
        file.close()
  return msg
