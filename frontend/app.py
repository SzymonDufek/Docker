from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join('uploads', file.filename))
            response = requests.post('http://backend:8000/ask/', files={'file': open(f'uploads/{file.filename}', 'rb')})
            classification_result = response.json()['result']
            return render_template('index.html', result=classification_result, filename=file.filename)
    return render_template('index.html', result=None, filename=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)