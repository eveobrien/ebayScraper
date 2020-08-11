import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.ebay.co.uk/itm/3-Wheeled-Scooter-Kids-Tri-Folding-Tilt-To-Turn-Adjustable-Push-Ride-On-RideStar/113846559710?var=414084765987&_trkparms=%26rpp_cid%3D5d8cce9aa937f33a775e44ce%26rpp_icid%3D5d8cce9aa937f33a775e44cd&_trkparms=pageci%3A4d48ccce-dbc8-11ea-a4ba-1e04fc6b3716%7Cparentrq%3Add57e7691730ad397ed861c2ffffa31c%7Ciid%3A1'
headers={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}


def send_mail():
    server = smtplib.SMTP('smtp.gmal.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('youremail@gmail.com', 'password')

    subject = 'Price decrease on product!'
    body = 'check ebay link https://www.ebay.co.uk/itm/3-Wheeled-Scooter-Kids-Tri-Folding-Tilt-To-Turn-Adjustable-Push-Ride-O'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'youremail@gmail.com',
        msg
    )

    print('email sent')
    server.quit()


def check_price():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="itemTitle").get_text()
    price=soup.find(id="prcIsum").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 2.400):
        send_mail()


    print(title.strip())
    print(price)


while(True):
    check_price()
    time.sleep(60 * 60)
