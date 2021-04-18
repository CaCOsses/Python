from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Linkedin:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Chrome(PATH_TO_BROWSER_DRIVER)