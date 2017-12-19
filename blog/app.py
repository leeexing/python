'''
my blog
'''
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>', methods=['GET'])
def user(name=None):
    return render_template('user.html', name=name)

@app.route('/register', methods=['GET'])
def register():
    return render_template('login/register.html')

if __name__ == "__main__":
    app.run(debug=True)
