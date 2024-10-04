from flask import Flask, jsonify
import os
import psycopg2

app= Flask(__name__)

@app.route('/api/data', methods= ['GET'])
def get_data():
    data= {
            'message': 'Hello from backend!',
            'status': 'success'
            }
    return jsonify(data)


if __name__== '__main__':
    app.run(host='0.0.0.0', port= 5002)
