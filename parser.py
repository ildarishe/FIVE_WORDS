import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = "https://vfrsute.ru/%D1%81%D0%BA%D0%B0%D0%BD%D0%B2%D0%BE%D1%80%D0%B4/%D1%81%D0%BB%D0%BE%D0%B2%D0%BE-%D0%B8%D0%B7-5-%D0%B1%D1%83%D0%BA%D0%B2/"
r = requests.get(URL_TEMPLATE)
print(r.text)
words = ""
soup = bs(r.text, "html.parser")
vacancies_info = soup.find_all('li', class_='words_group-item')

for info in vacancies_info:
    print(info.text)
    words += info.text + "\n"
with open("words.txt", "w", encoding="utf-8") as f:
    f.write(words)
