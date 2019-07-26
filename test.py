import requests
from bs4 import BeautifulSoup

url = 'https://www.lueftner-cruises.com/en/river-cruises/cruise.html'
response = requests.get(url).text
soup = BeautifulSoup(response)
# print(soup.prettify())

def get_cruises(html):
    result = []
    cruises = [i for i in soup.find_all('li', {'class': "cruise-item"})]
    for cruise in cruises:
        result.append({'name': get_cruise_name(cruise),
                       'days': get_cruise_date(cruise)})
    return result


def get_cruise_name(cruise):
    return cruise.find('span', {'class': "cruise-name"}).string


def get_cruise_date(cruise):
    print(cruise.findAll('span', {'class': "small-btn-font"}))
    return cruise.findAll('span', {'class': "cruise-from-price"})

print(get_cruises(soup))





# print(soup)

# def get_html(url):
#     response = requests.get(url)
#     return response.text
#
# def get_cruise_name(html):
#     soup = BeautifulSoup(html)
#     # print(soup.prettify())
#     for i in soup.find_all('span', {'class':"cruise-name"}):
#         print(i)
#
# def get_cruise_from_price(html):
#     soup = BeautifulSoup(html)
#     soup.prettify()
#     for i in soup.find_all('span', {'class':"cruise-from-price"}):
#         print(i)
#
# get_cruise_name(get_html(url))
# get_cruise_from_price(get_html(url))