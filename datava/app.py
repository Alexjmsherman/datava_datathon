__author__ = 'alsherman'

import json
import os
from flask import Flask, request, render_template, url_for, redirect
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import googlemaps
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
bootstrap = Bootstrap(app)
gmaps = googlemaps.Client(key='AIzaSyAb416HhO9hmtIBYR4Zl-zZ3QAF0m7nJGE')

initial_location = None


@app.route('/')
@app.route('/datathon/')
def index():
    # initiate the map at the VA library - location of hackathon
    return render_template('index.html', users_address=json.dumps(initial_location))


if __name__ == "__main__":
    app.debug = True
    app.run()
