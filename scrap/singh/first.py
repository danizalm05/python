#  https://www.youtube.com/watch?v=qgDBLD7EChI&list=PLmcBskOCOOFUmbUv0CIMuATDVKVrOhBMV&index=4
# Web Scraping with Python: Collecting Data from the Modern Web - O'Reilly Media
#

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


def getTitle(url):
    try:
      html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None

    print(bsObj.prettify())
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print("Title = ", title)



