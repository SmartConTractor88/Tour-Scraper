import requests # work with urls

import selectorlib # extract only specific information from the source code

import smtplib, ssl
import os
import time

# connect to database
import sqlite3
connection = sqlite3.connect("data.db")

url = "http://programmer100.pythonanywhere.com/tours/"

# id="displaytimer" # id code for the desired part

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return(source)


def extract(source):
    """"""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    
    value = extractor.extract(source)["tours"] # return the key "tours" from the dictionary 
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "zigmarszigmars19@gmail.com"
    password = os.getenv("JBN@gmail_APP_PASS_01")

    receiver = "zigmarszigmars19@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def store_extracted():
    row = extracted.split(",") # create a list
    row = [item.strip() for item in row] # remove spaces in each item
    # band, location, date = row
    cursor = connection.cursor()
    # each item to replace one question mark:
    cursor.execute("INSERT INTO events VALUES (?,?,?)", row)
    connection.commit()


def read_extracted():
    row = extracted.split(",") # create a list
    row = [item.strip() for item in row] # remove spaces in each item
    band, location, date = row


    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM events WHERE band=? AND location=? AND date=?", 
                   (band, location, date)) # execute SQL queries
    

    rows = cursor.fetchall()
    print(rows)
    return rows


if __name__ == "__main__":
    while True:
        scraped = scrape(url)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours": # if there is an event...
            row = read_extracted()
            if not row: # if the event is new...
                store_extracted()
                send_email(message="New event was found:") # send it on email
        time.sleep(5)

