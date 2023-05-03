from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
from datetime import datetime 
import pandas as pd
import time

filename = 'pre_base.csv'
data = pd.read_csv(filename, sep=',' ,names= ['cuota_local','cuota_empate','cuota_visitante','cuota_mas_2.5','cuota_menos_2.5','eq_local','eq_visitante','fecha','gol_local','gol_visitante'])

browser = webdriver.Firefox()
browser.implicitly_wait(60)
browser.get("https://www.google.com/?hl=es")
browser.implicitly_wait(60)


now = datetime.now()
now = time.strptime(now.strftime('%Y-%m-%d'), '%Y-%m-%d' )

for i in range(len(data)):
    if pd.isna(data.iloc[i,9]) and time.strptime(data.iloc[i,7], '%Y-%m-%d' ) < now :
        
        buscador = browser.find_element(By.ID,"APjFqb")
        busqueda = data.iloc[i, 5] + ' ' + data.iloc[i, 6] #+ ' ' + data.iloc[i, 7]
        buscador.clear()
        buscador.send_keys(busqueda, Keys.ENTER)
        time.sleep(3)
        gol_local = browser.find_element(By.CLASS_NAME, 'imso_mh__l-tm-sc')
        gol_local = gol_local.text
        gol_visitante = browser.find_element(By.CLASS_NAME, 'imso_mh__r-tm-sc')
        gol_visitante = gol_visitante.text
        data.iloc[i,8] = gol_local
        data.iloc[i,9] = gol_visitante

        
browser.close()  
data.to_csv('pre_base.csv', header=False, index=False)
data.to_csv('base.csv', header=False, index=False)