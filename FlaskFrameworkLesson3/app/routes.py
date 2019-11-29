from flask import render_template, flash, redirect,url_for
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        flash('Вход запрошен для пользователя {}, запомнить = {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Вход', form=form)
