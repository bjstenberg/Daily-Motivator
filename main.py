import smtplib
import random
# To get current time.
import datetime as dt

# SMTP = Simple Mail Transfer Protocol, all emailproviders have different SMTP codes.

MY_EMAIL = "stenberg.p.b@gmail.com"
MY_PASSWORD = "##ThebigbadbearGmail89"

# Current date and time
now = dt.datetime.now()
# year = now.year
# month = now.month
day_of_week = now.weekday()
if day_of_week == 3:
    with open("quotes.txt", "r") as my_quotes_file:
        my_quotes = my_quotes_file.readlines()
        random_quote = random.choice(my_quotes)

    print(random_quote)
    # date_of_birth = dt.datetime(year= 1989, month=9, day=12, hour=2)
    # print(date_of_birth)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # Transport Layer Security - TLS
    #   If email goes avr, it gets encrypted so the third party can't read it
    #   I.e. it secures the connection to smtp
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        # Added encode UTF-8 to be able to send with Å Ä and Ö
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="aka_bps@hotmail.com",
            msg=f"Subject: Daily Motivator!\n\nThis is your daily motivation!\n{random_quote}")
        #   msg="Subject: Älskling!\n\nJag löste det så jag kan skicka med svenska bokstäver!.encode("utf-8"))

connection.close()
