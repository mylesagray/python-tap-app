"""Runs a simple Flask web app to print out a static web page"""
import gunicorn
from flask import Flask, render_template, jsonify

APP_NAME = "Python App With Flask, HTML, And REST"
app = Flask(APP_NAME)
CLIENT = "VMlive"
FRAMEWORK = "Python with Pipenv"

messages = [
    {
        'client': CLIENT,
        'framework': FRAMEWORK,
        'msg_subject': 'Secure Software Supply Chains Are Great!',
        'msg_body': 'With A Secure Software Supply Chain, \
            Deploying Python Code To PROD is Safe, Reliable, And Fast!'
    }
]


@app.route("/")
def hello():
    """Renders the web page template and serves"""
    return render_template('index.html', client=CLIENT, framework=FRAMEWORK)


@app.route('/messages')
def get_incomes():
    """Fakes a json API"""
    return jsonify(messages)


@app.route('/versions')
def versions():
    """Prints out the current Gunicorn version"""
    gu_version = gunicorn.__version__
    return "Gunicorn version: " + gu_version


app.debug = False
