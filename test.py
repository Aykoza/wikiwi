import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup, SoupStrainer

URL = 'https://www.lueftner-cruises.com/en/river-cruises/cruise.html'
# URL2 = 'https://www.lueftner-cruises.com/en/river-cruises/cruise/show/tulip-serenade-2020.html'
DOMAIN_NAME = urlparse(URL).hostname
PROTOCOL = urlparse(URL).scheme


def parser(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    return soup


def get_cruises(url):
    html = parser(url)
    result = []
    cruises = [i for i in html.find_all('li', {'class': "cruise-item"})]
    for cruise in cruises:
        cruise_page = parser(get_cruise_link(cruise))
        # print(cruise_page.prettify())
        result.append({'name': get_name(cruise),
                       'days': get_date(cruise),
                       'itinerary': get_itinerary(cruise_page)})
    return result


def get_name(cruise):
    return cruise.find('span', {'class': "cruise-name"}).string


def get_date(cruise):
    date = cruise.find('span', {'class': "cruise-from-price"}).next
    date = re.search("\d+", date).group(0)
    return date


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



print(get_cruises(URL))
