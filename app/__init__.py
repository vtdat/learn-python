from flask import Flask
import json

app = Flask(__name__)
app.url_map.strict_slashes=True

@app.route('/json/')
def index():
  return json.dumps(os.listdir(os.path.join(app.root_path, 'data')))

