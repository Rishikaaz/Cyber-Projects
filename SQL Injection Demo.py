# Flask App 
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{user}' AND password='{pwd}'"
        cursor.execute(query)
        if cursor.fetchone():
            return "Login Success"
        else:
            return "Login Failed"
    return '''
        <form method="post">
            Username: <input name="username">
            Password: <input name="password">
            <input type="submit">
        </form>
    '''
