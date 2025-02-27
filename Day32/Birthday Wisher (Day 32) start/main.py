import datetime as dt
import random
import smtplib

# import smtplib
#
my_email = "mariannabenkalovych@gmail.com"
password = "llaeujmlwudwuccg"
#
# with  smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="zirochkamaym@gmail.com", msg="Subject:Hello\n\n The body.")
#
# # connection.close()
# now = dt.datetime.now()
# year = now.weekday()
# print(year)

# --------------------- Send Motivation Quotes on Monday via Email ----------------------
now = dt.datetime.now()

weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt", mode="r") as file:
            lines = file.readlines()
            quote = random.choice(lines)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,  msg=f"{quote}")





