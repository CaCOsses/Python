import urllib.request
import sys
from bs4 import BeautifulSoup

datos = urllib.request.urlopen('https://es.linkedin.com/learning/python-para-data-scientist-avanzado/desafio-web-scraping-y-modelizacion').read().decode()
soup =  BeautifulSoup(datos)
print(soup.get_text())