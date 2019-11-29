from flask import Flask, url_for, request, send_file, redirect, abort

app = Flask(__name__)  # main


# @app.route(rule, options)

@app.route('/')
@app.route('/index')
def main_page():
    return 'Привет мир'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Привет, %s' % name


@app.route('/catalog/<int:item_id>')
def catalog_item(item_id):
    return 'Номер в каталоге: %d' % item_id


@app.route('/version/<float:vertion>')
def versions(version):
    return 'Номер версии: %f' % version


@app.route('/path1/')
def path1():
    return 'Это маршрут 1'


@app.route('/path2')
def path2():
    return 'Это маршрут 2'


@app.route('/url_for-test')
def url_for_test():
    return url_for('main_page')


@app.route('/login.html')
def send_login():
    return send_file('login.html')


# url_for('static', filename = 'static.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return 'Запрос методом POST, переданное значение: %s' % user
    else:
        user = request.args.get('name')
        return 'Запрос методом GET, переданное значение: %s' % user


@app.route('/redirect-to-login-page')
def redirected():
    return redirect(url_for('send_login'))


@app.route('/aborted-page')
def aborted_page():
    abort(401)
    this_is_never_executed()


@app.errorhandler(404)
def page_not_found(error):
    return 'Такое страницы не существует!', 404


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('main_page'))
        print(url_for('path1'))
        print(url_for('path2'))
    app.run(port=8080, debug=True)
