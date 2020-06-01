from flask import Flask, render_template, request, redirect
import pandas as pd
from predict import getRegressionFunction

ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    elif request.method == 'POST':
        if 'file' not in request.files:
            print('failed, no file in request')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            print('failed, no file name')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            print('file read')
            dataFrame = pd.read_csv(file)
            print(dataFrame.head())
            # newFunction = getRegressionFunction(dataFrame)
            # print(newFunction)
            return redirect(request.url)

if __name__ == "__main__":
    app.run()