import smtplib
from datetime import *
from random import *
import pandas

PLACEHOLDER = "[NAME]"

my_email = "example@gmail.com"
password = "example"

now = datetime.now()
day_of_week =  now.day
month = now.month

random_letter = random.randint(1, 3)

data = pandas.read_csv("Day 32 Send Mail/Birthday WIsher/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

print(birthdays_dict)

with open("Day 32 Send Mail/Birthday WIsher/birthdays.csv") as birthdays:
    data = pandas.read_csv(birthdays)
    data_dict = data.to_dict()
    data_frame = pandas.DataFrame(data_dict)

for (index, row) in data_frame.iterrows():
    if row.day == day_of_week and row.month == month:
        person = str(row.names)
        with open(f"Day 32 Send Mail/Birthday WIsher/letter_templates/letter_{random_letter}.txt") as letter_file:
            letter_contents = letter_file.read()
            new_letter = letter_contents.replace(PLACEHOLDER, person)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="pycourse@hotmail.com", msg=f"subject:Happy Birthday\n\n{new_letter}")




