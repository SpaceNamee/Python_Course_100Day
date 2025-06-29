from flask import Flask, render_template, request, redirect, url_for

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

all_books = []


@app.route('/')
def home():
    print(all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = request.form["book"]
        author = request.form["author"]
        rate = request.form['rate']
        about_book = {
            "title": new_book,
            "author": author,
            "rating": rate    
        }
        print(about_book)
        all_books.append(about_book)
        return redirect(url_for('home'))
    
    return render_template('add.html' )
    


if __name__ == "__main__":
    app.run(debug=True)

