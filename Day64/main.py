from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests


API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYzQxZGU5ZTgyYzM0ZDZmNDkzYjA0ODJjNGExNTRjOSIsIm5iZiI6MTc1MTMxNjAwNi44MjUsInN1YiI6IjY4NjJmNjI2MThkMmQ5YjA4ZDA4OTM2MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ud-9tTEYkDvwImZoKRaofQ9oCtKhZ511P9G7R2_6W8I"
API_KEY = "bc41de9e82c34d6f493b0482c4a154c9"

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
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=True)

class AddMovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

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
    books = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
    return render_template("index.html", books = books)

@app.route("/update/<idx_book>", methods=["POST", "GET"])
def update(idx_book):
    form = EditForm()
    book = db.session.execute(db.select(Movie).where(Movie.id == int(idx_book))).scalar()

    if book == None:
        return redirect(url_for('home'))
    if request.method == "POST":
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

    if request.method == "POST":
        url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYzQxZGU5ZTgyYzM0ZDZmNDkzYjA0ODJjNGExNTRjOSIsIm5iZiI6MTc1MTMxNjAwNi44MjUsInN1YiI6IjY4NjJmNjI2MThkMmQ5YjA4ZDA4OTM2MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ud-9tTEYkDvwImZoKRaofQ9oCtKhZ511P9G7R2_6W8I"
        } 
        params = {
            "query": form.title.data,
        }

        response = requests.get(url, headers=headers, params=params)
        titles = [(res['original_title'],res['release_date'],res['id'] ) for res in response.json()['results']]
        return render_template('select.html', movies = titles)
   

    return render_template('add.html', form=form)
    
@app.route("/add_by_id/<id>")
def add_movie_id(id):
    form = EditForm()   
    if request.method == "POST":
        rating = form.rating.data
        review = form.review.data

        movie = db.session.execute(db.select(Movie).where(Movie.id == int(id))).scalar()
        movie.rating = rating
        movie.review = review
        db.session.commit()

        return redirect(url_for('home'))
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYzQxZGU5ZTgyYzM0ZDZmNDkzYjA0ODJjNGExNTRjOSIsIm5iZiI6MTc1MTMxNjAwNi44MjUsInN1YiI6IjY4NjJmNjI2MThkMmQ5YjA4ZDA4OTM2MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ud-9tTEYkDvwImZoKRaofQ9oCtKhZ511P9G7R2_6W8I"
    } 

    response = requests.get(url, headers=headers)
    data = response.json()

    title = data['original_title']
    year = data['release_date']
    description = data['overview']
    img_url = f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    rating = data['vote_average']
    review = "None"

    db.session.add(Movie(title=title, year=year, description=description, img_url=img_url, rating=rating, review=review))
    db.session.commit()

    idx_book = db.session.execute(db.select(Movie).where(Movie.title == title)).scalar().id
    return redirect(url_for('update', idx_book=idx_book))



if __name__ == '__main__':
    app.run(debug=True)
