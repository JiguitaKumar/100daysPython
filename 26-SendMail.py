import random
import smtplib
import datetime as dt
import pandas

# ------------------------- HOW TO WORK WITH SMTP -------------------------
my_email = "test@gmail.com"
password = "randompassword"

# how to connect with the email server
connection = smtplib.SMTP("smtp.gmail.com")
# secures the connection to the email server so that no one can read it
connection.starttls()
# log in to our email service
connection.login(user=my_email, password=password)
# define the sender, recipient addresses and message for the email we're sending
connection.sendmail(from_addr=my_email, to_addrs="test@yahoo.com", msg="Subject:Hello World\n\nThis is the body of my email.")
# close connection
connection.close()

# a simpler way to create a connection without having to close it
with smtplib.SMTP("smtp.gmail.com") as connection2:
    connection2.starttls()
    connection2.login(user=my_email, password=password)
    connection2.sendmail(from_addr=my_email, to_addrs="test@yahoo.com", msg="Subject:Hello World\n\nThis is the body of my email.")



# ------------------------- HOW TO WORK WITH DATETIME -------------------------
# current date and time
now = dt.datetime.now()
print(now)
print(now.year)

# saving a date and time
date_of_birth = dt.datetime(year=1989, month=6, day=26, hour=18)
print(date_of_birth)



# ------------------------- CHALLENGE 1 - SEND QUOTE ON MONDAYs -------------------------
day_of_the_week = dt.datetime.now().weekday()

def send_msg():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        random_quote = random.choice(quotes_list)
        connection.sendmail(from_addr=my_email, to_addrs="example@yahoo.com", msg=f"Subject:Motivation Quote\n\n{random_quote}")

if day_of_the_week == 2:
    with open("quotes.txt", "r") as f:
        quotes_list = f.readlines()
    send_msg()
    print(random.choice(quotes_list))



# ------------------------- CHALLENGE 2 - BIRTHDAY WISHER -------------------------
month = dt.datetime.now().month
day = dt.datetime.now().day

df = pandas.read_csv("./birthdays.csv")
bday_dict = df.to_dict(orient="records")
print(bday_dict)

for record in bday_dict:
    print(record)
    if month == record["month"] and day == record["day"]:
        random_letter = random.randint(1, 3)
        with open(f"./letter_templates/letter_{random_letter}.txt", "r") as f:
            message = f.read()
            message = message.replace("[NAME]", record["name"])
            print(message)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=record["email"], msg=f"Subject:Happy Birthday!!\n\n{message}")
