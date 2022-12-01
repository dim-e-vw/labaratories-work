import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="lab4",
                        user="postgres",
                        password="573169",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            if username == "":
                return "Введите логин!"
            password = request.form.get('password')
            if password == "":
                return "Введите пароль!"
            try:
                cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s",
                               (str(username), str(password)))
                records = list(cursor.fetchall())
                return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
            except Exception as E:
                print(E)
                return "Вас нет в базе данных!"
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
