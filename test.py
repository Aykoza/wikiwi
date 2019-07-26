import requests
from bs4 import BeautifulSoup

url = 'https://www.lueftner-cruises.com/en/river-cruises/cruise.html'


def get_html(url):
    response = requests.get(url)
    return response.text

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')
    links = []
    for td in tds:
        a = td.find('a', class_='currency-name-container').get('href')
        link = 'https://coinmarketcap.com' + a
        links.append(link)
    return links

print(get_html(url))