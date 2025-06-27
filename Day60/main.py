from flask import Flask, render_template, request
import requests
import smtplib

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
OWN_EMAIL = os.environ['EMAIL_ADDRESS']
OWN_PASSWORD = 'ialu lsyr knkc xyso'

app = Flask(__name__)   
@app.route('/lesson60')
def index1():
    return render_template('login.html')

@app.route('/lesson60/login', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
    return render_template('index1.html', username=username, password=password)


price = requests.get("https://api.npoint.io/5a6b0c6f8782603fc9b9").json()
print(price["cot-1"]['name'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def show_about(price=price):
    return render_template('about.html', price = price)

@app.get('/contact/')
def show_contact():
    if request.method == "GET":
        return render_template('contact.html') 

@app.post('/contact/')
def succsess_page():
    if request.method == "POST":
        firstName = request.form['firstName']
        lastName = request.form["lastName"]
        username = request.form['username']
        email = request.form['email']
        address = request.form["address"]
        address2 = request.form['address2']
        country = request.form['country']
        state = request.form['state']
        zip_ = request.form['zip']
        # save_info = request.form["save-info"]
        paymentMethod = request.form['paymentMethod']
        cc_name = request.form['cc-name']
        cc_number = request.form['cc-number']
        cc_expiration = request.form['cc-expiration']

        send_email(firstName, lastName, email, country)
        return render_template('success_contact.html', firstName=firstName, lastName=lastName, username=username, email=email, address=address, address2=address2, country=country, state=state, zip_=zip_, paymentMethod=paymentMethod, cc_name=cc_name, cc_number=cc_number, cc_expiration=cc_expiration)
    
def send_email(firstName, lastName, email_, country ):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(
            from_addr = OWN_EMAIL,
            to_addrs = OWN_EMAIL,   
            msg = f"Subject:Client\n\nName: {firstName} {lastName}\nEmail: {email_}\nCountry: {country}"
        )   

if __name__ == "__main__":
    app.run(debug=True) 