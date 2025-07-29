from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import os
from sqlalchemy.exc import IntegrityError
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from typing import List

dir_path = os.path.join((os.path.dirname(os.path.abspath(__file__))), "instance")
'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id==user_id)).scalar_one_or_none()

# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dir_path}/posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(1000), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    comment_text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id = mapped_column(ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    blog_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"))
    post = relationship("BlogPost", back_populates="comments")

with app.app_context():
    db.create_all()

def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            if current_user.get_id() != "1":
                return abort(403)
            return func()    
        else:
            return login_manager.unauthorized()
    return wrapper  
    
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        if not email or not password or not name:
            flash("Please fill out all fields.")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(email=email, password=hashed_password, name=name)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash("successful! Please log in.")
            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            flash("Email already exists. Please use a different email.")
    return render_template("register.html", form=form)


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = request.form.get('email')
            password = request.form.get('password')

            # if not email or not password:
            #     error = "Please fill out all fields."
            #     return redirect(url_for('login'), error=error)

            user = db.session.execute(db.select(User).where(User.email == email)).scalar_one_or_none()
            if user and check_password_hash(user.password, password):
                login_user(user)
                flash("Successfully logged in!")
                return redirect(url_for('get_all_posts'))
            else:
                error = 'Invalid email or password'
                return render_template("login.html", form=form, error=error)
    return render_template("login.html", form=form)


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated, user=current_user)


# TODO: Allow logged-in users to comment on posts

@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)
    if request.method == "POST":
        if form.validate_on_submit():
            if not current_user.is_authenticated:
                flash("You need to be logged in to comment.")
                return redirect(url_for('login'))
            comment = form.comment.data
            if not comment:
                flash("Comment cannot be empty.")
                return redirect(url_for('show_post', post_id=post_id))
            comment_example = Comment(comment_text=comment, blog_id=post_id, author_id=current_user.get_id())
            try:
                db.session.add(comment_example)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                flash("Error saving comment. Please try again.")
                return redirect(url_for('show_post', post_id=post_id))
            
            flash("Comment submitted successfully!")
            return redirect(url_for('show_post', post_id=post_id))
    comments = db.session.execute(db.select(Comment).where(Comment.blog_id == int(post_id))).scalars().all()
    return render_template("post.html", post=requested_post, form=form, comments=comments, logged_in=current_user.is_authenticated)


@admin_only
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            date=date.today().strftime("%B %d, %Y"),
            author_id=current_user.get_id()
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, logged_in=current_user.is_authenticated)

@admin_only
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data

        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, logged_in=current_user.is_authenticated)

@admin_only
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, int(post_id))
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)


@app.route("/contact")
def contact():
    return render_template("contact.html", logged_in=current_user.is_authenticated  )


if __name__ == "__main__":
    app.run(debug=True, port=5002)
