import requests # work with urls

import selectorlib # extract only specific information from the source code

import smtplib, ssl
import os

url = "http://programmer100.pythonanywhere.com/tours/"

id="displaytimer" # id code for the desired part

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
    with open("data.txt", "a") as file:
        file.write(extracted+"\n")


def read_extracted():
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    scraped = scrape(url)
    extracted = extract(scraped)
    print(extracted)
    content = read_extracted()
    if extracted != "No upcoming tours": # if there is an event...
        if extracted not in content: # if the event is new...
            store_extracted()
            send_email(message="New event was found:") # send it on email


