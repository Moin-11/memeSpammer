# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from bs4 import BeautifulSoup
import requests
import time
import smtplib
from email.message import EmailMessage

BASE_URL = 'https://imgflip.com/i/'

HTMLTEMPLATE = '<div><img src = {} /></div>'
USER = 'me@gmail.com'
PASSWORD = 'PASSWORD'
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
DELAY = 5  # seconds


def getRandomMeme():

    response = requests.get(BASE_URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        img_url = 'https:'+ soup.find('img', id='im')['src']
    except:
        img_url = 'https:' + soup.find('video', id='vid')['poster']

    return img_url


def createEmail(recipients):
    img_url = getRandomMeme()
    html_body = HTMLTEMPLATE.format(img_url)
    msg = EmailMessage()
    msg['From'] = 'me@gmail.com'
    msg['To'] = ",".join(recipients)
    msg['Subject'] = "get Back To Work!"
    msg.set_content(html_body, subtype='html')
    return msg

def sendRandomMeme(recipients):
    server = smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT)
    server.starttls()
    server.login(USER, PASSWORD)

    msgcnt = 0

    while True:
       try:

        message = createEmail(recipients)
        server.send_message(message)
        msgcnt += 1
        print(f'Message =  + (msgcnt)')
        time.sleep(DELAY)
       except KeyboardInterrupt:
           server.close()
           break


sendRandomMeme(['you@gmail.com', 'you_2@gmail.com'])