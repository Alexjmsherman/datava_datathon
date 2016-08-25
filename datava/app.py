__author__ = 'alsherman'

import json
import pandas as pd
from flask import Flask, request, render_template, url_for, redirect
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import googlemaps
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
bootstrap = Bootstrap(app)
gmaps = googlemaps.Client(key='AIzaSyAb416HhO9hmtIBYR4Zl-zZ3QAF0m7nJGE')

initial_location = None


### import skill survey data
skill_names = pd.read_csv(r'C:\Users\alsherman\Desktop\Programming\hackathon\skills_df.txt')
skill_names_list = skill_names.columns[1:]


### FORMS

class Survey(Form):
    """ Survey questions including all skills for a user to provide personal ratings  """
    q0 = IntegerRangeField(label=skill_names_list[0], default=0,
                           validators=[NumberRange(min=0, max=5)])


### ROUTES
@app.route('/')
@app.route('/datathon/')
def index():
    # initiate the map at the VA library - location of hackathon
    return render_template('index.html', users_address=json.dumps(initial_location))


@app.route('/skills_survey/', methods=['GET', 'POST'])
def skills_survey():
    form = Survey()

    if request.method == 'POST':
        if form.validate_on_submit():
            q0 = form.q0.data

    return render_template('skills_survey.html', form=form)

if __name__ == "__main__":
    app.debug = True
    app.run()
