from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year : Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable= False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=True)

class AddMovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])

class EditForm(FlaskForm):
    rating = FloatField("Rating", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField("Update Movie")

def create_app():
    with app.app_context():
        db.create_all()

@app.route("/")
def home():
    create_app()
    # example_movie = Movie(title="Example Movie 3", year=2023, description="This is an example movie 2.", rating=8.5, ranking=1, review="Great movie!", img_url="/static/img/f.jfif")
    # db.session.add(example_movie)
    # db.session.commit()
    books = db.session.execute(db.select(Movie)).scalars().all()
    return render_template("index.html", books = books)

@app.route("/update/<idx_book>", methods=["POST", "GET"])
def update(idx_book):
    form = EditForm()
    book = db.session.execute(db.select(Movie).where(Movie.id == int(idx_book))).scalar()

    if book == None:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        book.rating = form.rating.data
        book.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    title = book.title
    return render_template("edit.html", book_title=title, form = form)

@app.route("/delete/<idx_book>", methods=["GET"])
def delete(idx_book):
    book = db.session.execute(db.select(Movie).where(Movie.id == int(idx_book))).scalar()
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["POST", "GET"] )
def add_():
    form = AddMovieForm()
    return render_template('add.html', form=form)
    # if request.method == "POST":
        
        # new_book = request.form["book"]
        # year = request.form["year"]
        # description = request.form["description"]
        # rating = request.form['rating']
        # review = request.form['review']
        # img_url = request.form['img_url']

        # new_movie = Movie(title=new_book, year=year, description=description, rating=rating, review=review, img_url=img_url)
        
        # with app.app_context():
        #     db.create_all()
        #     db.session.add(new_movie)  
        #     db.session.commit()

        # return redirect(url_for('home'))
    
    
if __name__ == '__main__':
    app.run(debug=True)
