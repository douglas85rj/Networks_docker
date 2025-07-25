import flask
from flask import request, jsonify
import requests
from flask_mysqldb import MySQL

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['MYSQL_HOST'] = 'host.docker.internal'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = '280903'
app.config['MYSQL_DB'] = 'flaskhost'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
    data = requests.get('https://randomuser.me/api/')
    return data.json()

@app.route("/inserthost", methods=['POST'])
def inserthost():
    data = requests.get('https://randomuser.me/api/').json()
    username = data['results'][0]['name']['first']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s)", (username,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User inserted successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
