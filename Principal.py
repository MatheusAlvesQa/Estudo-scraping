from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def getTittle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        tittle = bs.body.h1
    except AttributeError as e:
        return None

    return tittle

tittle = getTittle('http://www.pythonscraping.com/pages/page1.html')
if tittle == None:
    print('Titulo none')
else:
    print(tittle)