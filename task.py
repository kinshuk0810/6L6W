import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common import keys
import time
import csv

URL = "https://summerofcode.withgoogle.com/projects/"

driver = webdriver.Chrome('./chromedriver')
driver.get(URL)

time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

DATA=[]

table = soup.find('ul', attrs = {'toggle-list-group accordion-mode': 'true'})

for row in table.findAll('div', attrs = {'class': 'pos-rel'}):
    data = {}
    data['name'] = row.h2.text
    data['organisation'] = row.div.a.text
    data['project'] = row.div['ng-if'].a.text
    DATA.append(data)

filename = 'gsoc2021.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['name','organisation','project'])
    w.writeheader()
    for data in DATA:
        w.writerow(data)

driver.close()