import json
from flask import request, jsonify, Flask
import os
app = Flask(__name__)
app.config["DEBUG"] = True
#data= 'data.json'
users_dict = []
check=[0,0]
# List all users
@app.route('/users', methods=['GET'])
def get_users():
    if check[1]==0:
        data = 'data.json'
        path = os.path.join(app.root_path, 'Data', data)
        f = open(path, 'r')
        users_dict1 = json.load(f)
        users = []
        for user in users_dict1:
            contProp = 0
            for arg in request.args:
                val = user[arg]
                param = request.args[arg]
                if isinstance(val, int):
                    param = int(param)
                if isinstance(val, str):
                    val = val.upper()
                    param = param.upper()
                if val == param:
                    contProp += 1
            if contProp == len(request.args):
                users.append(user)
    if check[1]==1:
        users= users_dict[len(users_dict)-1]

    return jsonify(users)
# Get one user by id
@app.route('/user', methods=['GET'])
def get_user_by_id():
    # get parameter 'id' from request
    data = 'data.json'
    path = os.path.join(app.root_path, 'Data', data)
    f = open(path, 'r')
    users_dict1 = json.load(f)
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    for user in users_dict1:
        if user['id'] == id:
            return jsonify(user)
    return {}
# Get one user by id from the path
@app.route("/user/<id>", methods=['GET'])
def get_user_by_id_in_path(id):
    data = 'data.json'
    path = os.path.join(app.root_path, 'Data', data)
    f = open(path, 'r')
    users_dict1 = json.load(f)
    for user in users_dict1:
        if user['id'] == int(id):
            return jsonify(user)
    return {}
# Add new user
@app.route('/user', methods=['POST'])
def post_users():
    user = request.get_json()
    user['id'] = len(users_dict) + 1
    users_dict.append(user)
    check[1] = 1
    return jsonify(user)
@app.route('/users/restore', methods=['GET'])
def get_users1():
    check[1]=0
    return "restore sucessfully"
#Delete user by id
@app.route('/delete', methods=['DELETE'])
def delete_users():
    data = 'data.json'
    path = os.path.join(app.root_path, 'Data', data)
    a = os.path.isfile(path)
    if a == 0:
        return "File isn't existed"
    else:
        os.remove(path)
        return 'File is deleted'
@app.route('/json', methods=['PUT'])
def put():
  data = 'data.json'
  msg = ""
  path = os.path.join(app.root_path, 'Data', data)
  if not os.path.isfile(path):
    msg = "File not exists!"
  else:
    file = open(path, 'w')

    if file.write(json.dumps(request.json, indent=2)) == 0:
        msg = "Data should not be empty"
    else:
        msg = "OK"
    file.close()
  return msg
app.run()
# curl -H "Content-Type: application/json"  -XPOST -d '{"name":"Adam","age":14,"id":1}' http://localhost:5000/user
# curl -H "Content-Type: application/json"  -XPUT -d '[{"name":"Eva","age":14,"id":1}]' http://localhost:5000/json
# curl -X DELETE http://localhost:5000/delete
