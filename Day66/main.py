from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
import os
path_current_file = os.path.abspath(__file__)
path_current_dir = os.path.dirname(path_current_file)
path_instance = os.path.join(path_current_dir, "instance")
print(path_instance)
app = Flask(__name__, instance_path=path_instance)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
bd_path = os.path.join(path_instance, "cafes.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{bd_path}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/random', methods=['GET'])
def random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(cafes)
    # cafe = {"id":random_cafe.id,
    #         "name":random_cafe.name,
    #         "map_url":random_cafe.map_url, 
    #         "img":random_cafe.img_url, 
    #         "location":random_cafe.location, 
    #         "socket":random_cafe.has_sockets, 
    #         "toilet":random_cafe.has_toilet, 
    #         "wifi":random_cafe.has_wifi, 
    #         "can_take_calls":random_cafe.can_take_calls, 
    #         "seats":random_cafe.seats, 
    #         "coffee_price":random_cafe.coffee_price
    #         }
    
    return jsonify(cafe=random_cafe.to_dict())
    
@app.route("/all")
def all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify([{"cafe":cafe.to_dict()} for cafe in cafes])

@app.route("/search")
def search_by_location():
    query_location = request.args.get("loc")
    try:
        cafes = db.session.execute(db.select(Cafe).where(Cafe.location == query_location.capitalize())).scalars().all()
        if cafes == []:
            raise Exception
        cafe_list = [cafe.to_dict() for cafe in cafes]
        
    except Exception:
        return jsonify(error={"Not Found":"Sorry, we don't have a cafe at that location."}) 
    
    return jsonify(cafe_list)

@app.route('/add', methods=['POST'])
def add_cafe():
    if request.method == "POST":
        new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price "),
    )   
        
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route('/update-cafe/<id>', methods=["PATCH"])
def upadte_code(id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == int(id))).scalar_one_or_none()
        if cafe is None:
            raise Exception
        cafe.coffee_price = new_price
        db.session.commit()
    except Exception:
        error = {
            "faild":"Faild attempt to do patching."
        }
        return jsonify(error=error)
    
    return jsonify(cafe=cafe.to_dict())


@app.route('/delete/<id>', methods=['DELETE'])
def delete_cafe(id):
    api = request.args.get('api_key')
    if api == "TopSecretAPIKey":
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == int(id))).scalar_one_or_none()
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success="Cafe deleted successfully.")
        else:
            return jsonify(error={"Not found":"Such cafe is not found in data base."})
    else:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key."), 403
    
     
if __name__ == '__main__':
    app.run(debug=True)
