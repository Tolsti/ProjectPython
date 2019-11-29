from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tolsti'}
    posts = [
        {
            'author': {'username': 'Алексей'},
            'body': 'Привет!'
        },
        {
            'author': {'username': 'Михаил'},
            'body': 'Как дела!'
        },
        {
            'author': {'username': 'Юрий'},
            'body': 'Рад вас видеть!'
        }
    ]
    return render_template('index.html', title='Домашняя страница', user=user, posts=posts)
