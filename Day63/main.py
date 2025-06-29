from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author : Mapped[str] = mapped_column(String(250), nullable=False)
    review: Mapped[float] = mapped_column(Float, nullable=False)

all_books = []


@app.route('/')
def home():
    with app.app_context():
        db.create_all()
        db.session.commit()
        all_books = db.session.execute(db.select(Books)).scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = request.form["book"]
        author = request.form["author"]
        rate = request.form['rate']

        with app.app_context():
            db.create_all()
            db.session.add(Books(title=new_book, author=author, review=rate))  
            db.session.commit()

        # all_books.append(about_book)
        return redirect(url_for('home'))
    
    return render_template('add.html' )

@app.route("/delete")
def delete_books():
    with app.app_context():
        db.create_all()
        books_ = db.session.execute(db.select(Books)).scalars().all()
        for book in books_:
            db.session.delete(book)
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/change_rating/<idx_book>", methods=["POST", "GET"])
def change_rating(idx_book):
    print(idx_book)
    with app.app_context():
            db.create_all()
            book = db.session.execute(db.select(Books).where(Books.id==int(idx_book))).scalar()
    if request.method == "POST":
        new_rating = request.form["new_rating"]

        with app.app_context():
            db.create_all()
            book = db.session.execute(db.select(Books).where(Books.id==idx_book)).scalar()
            book.review = new_rating
            db.session.commit()

        return redirect(url_for('home'))
    
    return render_template('change_rating.html', book = book)

@app.route("/delete_book/<idx_book>")
def delete_book(idx_book):
    with app.app_context():
        db.create_all()
        book = db.session.execute(db.select(Books).where(Books.id==idx_book)).scalar()
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)

