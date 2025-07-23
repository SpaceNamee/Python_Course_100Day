from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, UserMixin

# CREATE LOGIN MANEGER
login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# INITIALIZE LOGIN MANAGER
login_manager.init_app(app)
# PATH
file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
db_path = os.path.join(dir_path, "instance")
files_path = os.path.join(dir_path, "static")
files_path = os.path.join(files_path, "files")
files_path = os.path.join(files_path, "cheat_sheet.pdf")
# CREATE DATABASE

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}/users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))



@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id==user_id)).scalar_one_or_none()


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        pass_ = request.form.get("password")

        new_user = User(
            name = name,
            email = email,
            password = generate_password_hash(password=pass_, method='pbkdf2:sha256',
            salt_length=8)
        )
        login_user(new_user)
        flash("Successfully registered and logged in!")
        db.session.add(new_user)

        db.session.commit()

        return render_template("secrets.html", name=name)
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.session.execute(db.select(User).where(User.email==email)).scalar_one_or_none()
        print(user.name)
        if user and check_password_hash(user.password, password):
            login_user(user)
            print("Successfully logged in!")
            return redirect(url_for('secrets', name=user.name), )
        else:
            print("Login failed. Please check your email and password.")
    return render_template("login.html")


@app.route('/secrets/<name>')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    app.config["FILES_PATH"] = 'static/files'
    return send_from_directory(directory =app.config["FILES_PATH"], path="cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
