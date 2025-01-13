from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/bye')
def bye():
    return "Goodbye"

@app.route('/users/<username>')
def users(username):
    return "Perfil de Usuario: " + username
