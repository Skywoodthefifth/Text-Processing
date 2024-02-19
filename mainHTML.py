import urllib.request as urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen("https://en.wikipedia.org/wiki/Sonic_the_Hedgehog")
html_doc = response.read()

soup = BeautifulSoup(html_doc, "html.parser")

strhtm = soup.prettify()

print(strhtm[:1000])

print(soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)
