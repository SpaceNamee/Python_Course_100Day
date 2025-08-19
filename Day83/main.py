from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, redirect, url_for, request
from wtforms import StringField, SubmitField, FloatField    
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")

