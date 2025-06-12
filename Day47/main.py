from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from smtplib import SMTP

# Load environment variables from .env file
load_dotenv()

url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find(name="span", class_="a-price-whole").getText() + soup.find(name="span", class_="a-price-fraction").getText()

# Get the product title
title = soup.find(id="productTitle").get_text().strip()

# Set the price below which you would like to get a notification
BUY_PRICE = 100
email = os.environ['EMAIL_ADDRESS']
password = os.environ['EMAIL_PASSWORD']


if float(price) < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    try:
        with SMTP("smtp.gmail.com",port=587 ) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            )
    except Exception as e:
        print(f"An error occurred: {e}")