import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import sys
from bs4 import BeautifulSoup

# Crear una sesión de Firefox
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.maximize_window()

# Acceder a la aplicación web
driver.get("http://www.linkedin.com")
driver.implicitly_wait(6)
driver.find_element_by_xpath("""//*[@id="session_key"]""").send_keys('XXXXX')
driver.find_element_by_xpath("""//*[@id="session_password"]""").send_keys('XXXXX')
driver.find_element_by_xpath("""//*[@class="sign-in-form__submit-button"]""").click()
driver.find_element_by_xpath("""//*[@class="global-nav__icon "]""").click()
driver.get("https://www.linkedin.com/learning/excel-crear-un-dashboard-intuitivo-e-impactante-desde-cero/cuadros-de-mando-o-dashboards-para-controlar-la-informacion")
elems = driver.find_elements_by_xpath("""//*[@id="vjs_video_3_html5_api"]""")
for elem in elems:
    print(elem)


