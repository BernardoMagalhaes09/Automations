from selenium import webdriver
import selenium
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
from selenium.webdriver.common.keys import Keys
from datetime import date


driver =  webdriver.Firefox()
driver.get('https://olx.com.br/')
search = driver.find_element(By.XPATH, '//input[@id="searchtext"]')
search.send_keys('Iphone 12')
search = driver.find_element(By.XPATH, f'//button[@class="searchSubmitBtn"]')
search.click()
anuncios = driver.find_elements(By.XPATH, '//a[@class="fnmrjs-0 fyjObc"]')
for anuncio in anuncios:
    url = anuncio.get_attribute('href')
    title = anuncio.get_attribute("title")
    img = anuncio.find_element(By.XPATH, '//img[@class="sc-101cdir-0 cldTqT"]').get_attribute('src')
    p = anuncio.find_element(By.XPATH, '//p[@class="sc-1iuc9a2-8 bTklot sc-ifAKCX eoKYee"]')
    d = anuncio.find_element(By.XPATH, '//div[p/@class="sc-1iuc9a2-3 kcOvhi sc-ifAKCX fWUyFm"]')
    date = d.text
    price = p.text
    print(image, title, url, price, date)
