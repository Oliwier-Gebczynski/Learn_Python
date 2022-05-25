import requests

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=EUR%2CUSD%2CCHF%2CGBP%2CCZK&base=PLN"

payload = {}
headers= {
  "apikey": ""
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

file = open('currencies', 'w')

file.write(result)

file.close()

print(result)