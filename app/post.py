from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__,template_folder='../templates')



@app.route('/upload')
def upload_file():
    return render_template('upload.html')



@app.route('/uploader', methods=[ 'POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "Your files is uploaded !!!"
    


if __name__ == '__main__':
    app.run(debug=True)