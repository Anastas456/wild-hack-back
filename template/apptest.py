from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def wall():
    with sqlite3.connect('db.sqlite') as conn:
        # курсор нужен для отправки запросов
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()

    return render_template('index.html', posts=posts)

@app.route('/save', methods=['POST'])
def save_post():
    name = request.form.get('name')
    text = request.form.get('text')

    if text and name:
        with sqlite3.connect('db.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO posts (name, text) VALUES (?, ?)", (name, text))
            # сохранить изменения
            conn.commit()

    return redirect('/')

app.run(debug=True)
