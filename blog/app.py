'''
my blog
'''
from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_bootstrap import Bootstrap
import pymongo
import os

client = pymongo.MongoClient('localhost', 27017)
user_db = client['myblog']['users']

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'hard to guess string'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    username = session.get('username')
    return render_template('index.html')

@app.route('/user/<name>', methods=['GET'])
def user(name=None):
    return render_template('user.html', name=name)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        user_isexist = user_db.find_one({'username': username})
        print(user_isexist)
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
            user_db.insert(new_user)
            return redirect(url_for('login'))
    else:
        return render_template('login/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        has_user = user_db.find_one({'username': username, 'password': password})
        print(has_user)
        if has_user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('用户名或密码错误！')
            return redirect(url_for('login'))
    else:
        return render_template('login/login.html')


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
