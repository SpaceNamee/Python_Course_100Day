from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
# The above line is a fix for a typo in the original code.
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5 # pip install bootstrap-flask
 
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.secret_key = 'kdfnsjsnfdsjkfnkdsfnsk'
bootstrap = Bootstrap5(app) # initialise bootstrap-flask 

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    pass_ = PasswordField(label='Password')
    submit_btn = SubmitField(label='Submit')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        email = form.email.data
        password = form.pass_.data
        if email == "admin@email.com" and password == "12345678":
            return render_template('success.html', email=email)
        else:
            return render_template('denied.html', message="Invalid credentials")
        
    return render_template('login.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)
