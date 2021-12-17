# TODO
# - stworzenie pliku html z danymi // ZROBIONE
# - zapoznanie sie z wysyłaniem email przez python
# - zrobienie listy email
# - wysyłanie email za każdym otworzeniem programu

import requests
import json
import apikey
import datetime

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
    # _________________HEAD___________________
    html_head = f'<head>  <meta charset="UTF-8"> <link rel="stylesheet" href="style.css"> </head>'
    # ________________BODY___________________
    html_body = '<body>' # otwarcie znacznika body
    html_logo = f'<h1 class="logo"> ogCode cryptoStats </h1>' # stworzenie logo/nazwy
    html_title = f'<h2 class="title"> Cena kryptowalut z {time.strftime("%x")} </h2>' # stworzenie tytułu
    html_ul = f'<ul class="list">' # lista kryptowalut
    for item in list:
        html_li = f'<li class="list_element"> {item} </li>' # stworzenie elementu li
        html_ul += html_li # dodanie elementu do ul
    html_ul += f'</ul>' # domkniecie ul
    html_link = f'<a class="link" href="https://github.com/Oliwier-Gebczynski"> ogCode GitHub </a>'
    html_body += html_logo + html_title + html_ul + html_link + '</body>'
    # ________________RESULT__________________
    html = html_head + html_body
    # ________________SAVE FILE_______________
    file = open("html/index.html", "w")
    file.write(html)
    file.close()

create_html(get_data())




