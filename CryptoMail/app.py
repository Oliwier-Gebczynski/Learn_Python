import requests
import smtplib
import json
import apikey
import email_login
import datetime
from email.message import EmailMessage


login = email_login.login
password = email_login.password

def get_data():
    result_list = []

    headers = {
        'X-CMC_PRO_API_KEY': apikey.key,
        'Accepts': 'application/json'
    }

    params = {
        'start': '1',
        'limit': '5',
        'convert': 'PLN'
    }

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    json = requests.get(url, params=params, headers=headers).json()
    coins = json['data']

    for coin in coins:
        result = f"{coin['name']} ({coin['symbol']}):    Cena {coin['quote']['PLN']['price']} pln,    Zmiana przez 24 godziny: {coin['quote']['PLN']['percent_change_24h']}%"
        result_list.append(result)

    return result_list

def create_html(list):
    time = datetime.datetime.now()
    css = open("html/style.css").read()
    # _________________HEAD___________________
    html_head = f'<head>  <meta charset="UTF-8"> <style> {css} </style> </head>'
    # ________________BODY___________________
    html_container = '<div class="container"> '
    html_body = '<body>' # otwarcie znacznika body
    html_logo = f'<h1 class="logo"> ogCode cryptoStats </h1>' # stworzenie logo/nazwy
    html_title = f'<h2 class="title"> Cena kryptowalut z {time.strftime("%x")} </h2>' # stworzenie tytułu
    html_ul = f'<ul class="list">' # lista kryptowalut
    for item in list:
        html_li = f'<li class="list_element"> {item} </li>' # stworzenie elementu li
        html_ul += html_li # dodanie elementu do ul
    html_ul += f'</ul>' # domkniecie ul
    html_link = f'<a class="link" href="https://github.com/Oliwier-Gebczynski"> ogCode GitHub </a>'
    html_container += html_logo + html_title + html_ul + html_link + '</container>'
    html_body += html_container + '</body>'
    # ________________RESULT__________________
    html = html_head + html_body
    # ________________SAVE FILE_______________
    file = open("html/index.html", "w")
    file.write(html)
    file.close()

def send_email(to, login, password):
    message = EmailMessage()
    message['subject'] = "Daily crypto price by ogCode"
    message['from'] = login
    message['to'] = to
    html_message = open("html/index.html").read()
    message.add_alternative(html_message, subtype = "html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.ehlo()
            smtp.login(login, password)
            smtp.send_message(message)

create_html(get_data())
send_email("kolfolly@gmail.com", login, password)

