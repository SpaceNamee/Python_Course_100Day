import random
import smtplib
import pandas
import datetime as dt

now = dt.datetime.now()
month = now.month
day = now.day

my_email = "mariannabenkalovych@gmail.com"
password = "llaeujmlwudwuccg"

file = pandas.read_csv("birthdays.csv")
match_birth = file[file["day"] == day][file["month"] == month].to_dict(orient="records")
print(match_birth)

for i in range(len(match_birth)):
    letter_num = random.randint(1,3)
    person_email = match_birth[i]["email"]
    person_name = match_birth[i]["name"]

    with open(f"letter_templates/letter_{letter_num}.txt") as file:
        letter = file.read()

    try:
        letter = letter.replace("[NAME]", person_name)
    except:
        print("For everyone")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=person_email, msg=f"Subject:HappyBirthday! \n\n{letter}")
