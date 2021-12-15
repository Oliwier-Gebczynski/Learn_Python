# TODO
# - stworzenie pliku html z danymi
# - dodanie zdjec (logo) do kryptowalut
# - zapoznanie sie z wysyłaniem email przez python
# - zrobienie listy email
# - wysyłanie email za każdym otworzeniem programu

import requests
import json
import apikey

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
        result = f"{coin['name']} ({coin['symbol']}): Price {coin['quote']['PLN']['price']} pln, Change in 24 hours: {coin['quote']['PLN']['percent_change_24h']}%"
        result_list.append(result)

    return result_list

