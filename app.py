from flask import Flask, render_template, request, redirect
import sqlite3
import datetime
import time

app = Flask(__name__)

Questionnaire = []

@app.route('/')
def wall():
    with sqlite3.connect('db.sqlite') as conn:
        # курсор нужен для отправки запросов
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Questionnaire")
        posts = cursor.fetchall()

    return render_template('index.html', posts=posts)

@app.route('/save', methods=['POST'])
def save_post():
    id = request.form.get('id')
    name = request.form.get('name')
    email = request.form.get('email')
    birth_year = request.form.get('birth_year')
    phone_number = request.form.get('phone_number')
    education = request.form.get('education')
    desired_work_area = request.form.get('desired_work_area')
    arrival_date = request.form.get('arrival_date')
    departure_date = request.form.get('departure_date')
    languages = request.form.get('languages')
    experience = request.form.get('experience')
    recommendations = request.form.get('recommendations')
    skills = request.form.get('skills')
    voluntary_passport = request.form.get('voluntary_passport')
    reason = request.form.get('reason')
    video_link = request.form.get('video_link')
    comments = request.form.get('comments')

    if id and name and email and birth_year and phone_number and education and education and desired_work_area and arrival_date and departure_date and languages and experience and recommendations and skills and voluntary_passport and reason and video_link and comments:
        with sqlite3.connect('db.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Questionnaire (id, name, email, birth_year, phone_number, education, desired_work_area, arrival_date, departure_date, languages, experience, recommendations, skills, voluntary_passport, reason, video_link, comments) VALUES (?, ?)", (id, name, email, birth_year, phone_number, education, 
desired_work_area, arrival_date, departure_date, languages, experience, recommendations, skills, voluntary_passport, reason, video_link, comments))
            # сохранить изменения
            conn.commit()    

app.run(debug=True)






