from datetime import datetime
import pandas
import random
import smtplib
import os

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "your_pass"
today = datetime.now()
today_tuple = (today.month, today.day)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "birthdays_sample.csv")

data = pandas.read_csv(file_path)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = os.path.join(BASE_DIR, "letter_templates",f"letter_{random.randint(1,3)}.txt")
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
