from flask import Flask
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
    except:
      msg = "Something went wrong!"
  return msg

