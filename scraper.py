import requests
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/Apple-MacBook-Pro-9th-Generation-Intel-Core-i9/dp/B07SDPJ531/ref=sr_1_3?keywords=macbook+pro&qid=1564119110&s=gateway&sr=8-3"

headers = {"User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    price = price[2:10].replace(',','')

    print(price)
    converted_price = float(price)

    if(converted_price<230000) :
        send_mail()

    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('rajteknok@gmail.com', 'hellothere')

    subject = "Price Fell down"
    body = "check out amazon link = https://www.amazon.in/Apple-MacBook-Pro-9th-Generation-Intel-Core-i9/dp/B07SDPJ531/ref=sr_1_3?keywords=macbook+pro&qid=1564119110&s=gateway&sr=8-3"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'rajteknok@gmai.com',
        '17dec004@lnmiit.ac.in',
        msg
    )

    print('Email Sent')

    server.quit()

check_price()