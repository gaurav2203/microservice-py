from flask import Flask, render_template
import requests

app= Flask(__name__)

@app.route('/')
def index():
    response= requests.get('http://backend:5001/api/data')
    data= response.json()

    return render_template('index.html', data= data)

@app.route('/db')
def db():
    response= requests.get('http://backend:5001/api/db')
    data=response.json()

    return render_template('db.html', data= data)

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000)
