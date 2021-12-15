from bs4 import BeautifulSoup
import requests

name = input("Wpisz nazwę instagrama: ")
url = f"https://www.instagram.com/{name}/"
request = requests.get(url)
doc = BeautifulSoup(request.text, "html.parser")
meta = doc.find("meta", property = "og:description")
result_list = meta.attrs['content'].split(" ") #[ilosc_followersow, -, ilosc_folow, -, ilosc_postow, -, ...., nazwa_ig]

text = f"Name: {result_list[-1]}, Followers: {result_list[0]}, Following: {result_list[2]}, Posts: {result_list[4]}"

print(text)




