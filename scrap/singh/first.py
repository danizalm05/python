
# https://www.youtube.com/watch?v=U7tN6Zs2UY4&list=PLmcBskOCOOFUmbUv0CIMuATDVKVrOhBMV&index=6
# https://www.youtube.com/watch?v=GC890_Rco3g&list=PLmcBskOCOOFUmbUv0CIMuATDVKVrOhBMV&index=7
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

u1 = 'http://www.haarchion.co.il/poet/%d7%a9%d7%9c%d7%9e%d7%94-%d7%90%d7%91%d7%9f-%d7%92%d7%91%d7%99%d7%a8%d7%95%d7%9c/'
u2 = "http://www.pythonscraping.com/pages/page1.html"
title = getTitle(u2)
if title == None:
    print("Title could not be found")
else:
    print("Title = ", title)

u3 = "http://www.pythonscraping.com/pages/warandpeace.html"
html = urlopen(u3)
bsObj = BeautifulSoup(html, "lxml")
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())
#page 15 web scraping with  python

u4 = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(u4)
bsObj = BeautifulSoup(html, "lxml")
for child in bsObj.find('table', {'id': 'giftList'}).children:
   print(child)
#11