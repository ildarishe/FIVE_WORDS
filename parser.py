import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = "https://wotpack.ru/slova-iz-5-bukv-tinkoff-otvety-na-segodnja-nojabr/#_5"
r = requests.get(URL_TEMPLATE)
# print(r.text)
words = ""
soup = bs(r.text, "html.parser")
vacancies_info = soup.find_all('li')

for info in vacancies_info:
    print(info.text)
    words += info.text + "\n"
# with open("../FIVE_WORDS/words.txt", "w", encoding="utf-8") as f:
#     f.write(words)
