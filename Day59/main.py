from flask import Flask, render_template, url_for
import requests

price = requests.get("https://api.npoint.io/5a6b0c6f8782603fc9b9").json()
print(price["cot-1"]['name'])
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def show_about(price=price):
    return render_template('about.html', price = price)

@app.route('/contact/')
def show_contact():
    return render_template('contact.html')  

if __name__ == "__main__":
    app.run(debug=True)