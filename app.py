from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/bye')
def bye():
    return "Goodbye"

@app.route('/users/<username>')
def users(username):
    return "Perfil de Usuario: " + username
