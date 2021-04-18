from bs4 import BeautifulSoup
import requests

URL = "https://www.linkedin.com/learning/excel-crear-un-dashboard-intuitivo-e-impactante-desde-cero/la-hoja-auxiliar-del-dashboard"

# Realizamos la petición a la web
req = requests.get(URL).text

# Comprobamos que la petición nos devuelve un Status Code = 200
# print(req)
# Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
html = BeautifulSoup(req.text, "html.parser")
# Obtenemos todos los divs donde están las entradas
a = html.find_all('body')
b = a.find_all('script')