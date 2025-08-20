from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, redirect, url_for, request
from wtforms import StringField, SubmitField, FloatField    
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html", active_page="home")


@app.route("/projects/")
def projects():
    return render_template("projects.html", active_page="projects")

@app.route("/about_me/")
def about_me(): 
    return  render_template("about_me.html", active_page="about_me")

@app.route("/fqs/")
def fqs():
    return render_template("fqs.html", active_page="fqs")

@app.route("/contact/", methods=["GET", "POST"])
def contact():
    return render_template("contact.html", active_page="contact")

if __name__ == "__main__":
    app.run(debug=True)