import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.pythonscraping.com/pages/page3.html')

# print(data)
# print(data.text)

# html.parser : dom tree 깨진 경우 안될 수 있음
soup = BeautifulSoup(data.text, 'html.parser')

#gift1 > td:nth-child(1)

# print(soup)
gifts = soup.select('#giftList > .gift')
# print(gifts)

for g in gifts:
    tds = g.select('td')
    print(f"TITLE:{tds[0].text.strip()}, PRICE:{tds[2].text.strip()}")
    print(f"PIC: {tds[3].img['src']}")

gifts_title = soup.select('#giftList > .gift > td:nth-child(1)')
gifts_price = soup.select('#giftList > .gift > td:nth-child(3)')

def get_text(item):
    return item.text.strip()

gifts = dict(zip(map(get_text, gifts_title), map(get_text, gifts_price)))
print(gifts)
