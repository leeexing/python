'''
my blog
'''
from flask import Flask, render_template, redirect, url_for, flash, request, session, g
from flask_bootstrap import Bootstrap
from db import get_mongo_connection
import os
from datetime import timedelta

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
print(app.config['DEBUG'])
print(app.config['SECRET_KEY'])
print(app.config['MONGO_URI'])

bootstrap = Bootstrap(app)
db = get_mongo_connection().user



# app.config['SECRET_KEY'] = os.urandom(24)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'hard to guess string'
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
# session.permanent = True

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.before_request
def my_before_request():
    if not session.get('username') and request.endpoint not in ('login', 'register', 'static'):
        return redirect(url_for('login'))

@app.route('/')
def index():
    username = session.get('username')
    return render_template('index.html', username=username)

@app.route('/get')
def get_user():
    print(request.endpoint)
    print(request.endpoint in ('login', 'get', 'static'))
    username = session.get('username')
    param = request.args #获取get参数
    print(param)
    return render_template('user.html', name=username)

@app.route('/user/<name>', methods=['GET'])
def user(name=None):
    return render_template('user.html', name=name)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_isexist = db.user_db.find_one({'username': username})
        if user_isexist:
            flash('该用户名已被注册，请换一个用户名注册！')
            return render_template('login/register.html')
        else:
            new_user = {
                'username': username,
                'password': password,
                'isAdmin': False
            }
            session['username'] = username
            db.user_db.insert(new_user)
            return redirect(url_for('login'))
    else:
        return render_template('login/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.values)
        username = request.form.get('username')
        password = request.form.get('password')
        remember_me = request.form.get('rememberme') == 'on'
        print(remember_me)
        login_user = db.user_db.find_one({'username': username, 'password': password})
        print(login_user)
        if remember_me:
            session.permanent = True
        if login_user:
            session['username'] = username
            if login_user.get('isAdmin'):
                session['is_admin'] = True
            return redirect(url_for('index'))
        else:
            flash('用户名或密码错误！')
            return redirect(url_for('login'))
    else:
        return render_template('login/login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/article')
def article_list():
    return render_template('article/article_list.html')

@app.route('/article/:id')
def article_detail():
    return render_template('article/article_detail.html')

if __name__ == "__main__":
    app.run()
