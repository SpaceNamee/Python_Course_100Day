from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author : Mapped[str] = mapped_column(String(250), nullable=False)
    review: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

    db.session.add(Books(title="Harry", author="J.K. Rowling", review=9.5))  
    db.session.commit()