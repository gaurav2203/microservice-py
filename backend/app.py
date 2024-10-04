from flask import Flask, jsonify
import os
import psycopg2

app= Flask(__name__)
DATABASE_URL= os.getenv("DATABASE_URL")

@app.route('/api/data', methods= ['GET'])
def get_data():
    data= {
            'message': 'Hello from backend!',
            'status': 'success'
            }
    return jsonify(data)

def get_db_connection():
    conn= psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/api/db', methods=['GET'])
def get_db():
    conn= get_db_connection()
    cursor= conn.cursor()
    cursor.execute('SELECT name, email FROM users')
    users= cursor.fetchall()
    cursor.close()
    conn.close()

    data= [{'name': user[0], 'email': user[1]} for user in users]

    return jsonify({'status': 'success', 'users': data})

if __name__== '__main__':
    app.run(host='0.0.0.0', port= 5001)
