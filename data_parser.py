import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json


URL = 'https://www.lueftner-cruises.com/en/river-cruises/cruise.html'
DOMAIN_NAME = urlparse(URL).hostname   # Парсим домен для сборки круизного урла
PROTOCOL = urlparse(URL).scheme        # Парсим протокол для сборки круизного урла
HEADER = {'User-Agent': str(UserAgent().chrome)}


def parser(url):
    response = requests.get(url, headers=HEADER).text
    soup = BeautifulSoup(response, 'html.parser')
    return soup


def get_cruises(url, cruise_cnt=4):
    """
    Главная функция собирающая словарь с данными о круизе.
    В ней уже вызываются все остальные функции для сбора данных.
    Для удобочитаемости вынес все в отдельные функции.
    """
    html = parser(url)
    result = []
    cruises = html.find_all('li', {'class': "cruise-item"}, limit=cruise_cnt)
    for cruise in cruises:
        cruise_page = parser(get_cruise_link(cruise))
        result.append({'name': get_name(cruise),
                       'days': get_days(cruise),
                       'itinerary': get_itinerary(cruise_page),
                       'dates': get_date_price(cruise_page)})
    return result


def get_name(cruise):
    return cruise.find('span', {'class': "cruise-name"}).string


def get_days(cruise):
    days = cruise.find('span', {'class': "cruise-from-price"}).next
    days = re.search("\d+", days).group(0)
    return days


def get_cruise_link(cruise):
    link = '{}://{}{}'.format(PROTOCOL, DOMAIN_NAME, cruise.find('a', {'class': "cruise-link"})['href'])
    return link


def get_itinerary(cruise_page):
    itinerary = []
    itineraries = [i.string for i in cruise_page.find_all('span', {'class': "route-city"})]
    for i in itineraries:
        mix = i.split('>')
        mix = list(map(lambda x: x.strip(), mix))
        itinerary.append('>'.join(mix))
    return itinerary


def get_date_price(cruise_page):
    content = cruise_page.findAll('div', {'class': 'panel-heading main-cabin-heading'})
    dates = []
    for i in content:
        date = i.find('span', {'class': 'price-duration'}).string
        ship = i.find('span', {'class': 'table-ship-name'}).string
        price = i.find('span', {'class': 'big-table-font'}).string.strip()
        price = re.search('[\d,.]+', price).group(0)
        dates.append({date: {ship: price}})
    return dates


if __name__ == '__main__':
    # Сериализация в json для более наглядного представления данных
    print(json.dumps(get_cruises(URL), sort_keys=False, indent=4, ensure_ascii=False))