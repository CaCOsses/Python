from bs4 import BeautifulSoup
from lxml import html

import requests

URL = 'https://www.linkedin.com/learning/excel-crear-un-dashboard-intuitivo-e-impactante-desde-cero/la-hoja-auxiliar-del-dashboard'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html5lib')

results = soup.find(id="vjs_video_3")
print(results)