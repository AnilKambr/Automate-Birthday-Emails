from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "anilkambar114@gmail.com"
MY_PASSWORD = "stgckomczkdtwecf"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contest = letter_file.read()
        contest = contest.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connects:
        connects.starttls()
        connects.login(user=MY_EMAIL, password=MY_PASSWORD)
        connects.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contest}"
        )
