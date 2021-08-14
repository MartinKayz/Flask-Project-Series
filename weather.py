from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy





weather_app = Flask(__name__)

# loading enviroment variables from secret files
weather_app.config.from_pyfile('settings.py')


@weather_app.route('/')
def index():
    return render_template('weather.html')


