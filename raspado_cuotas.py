from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from datetime import datetime 
import time
 

def utf8_eq (equipo):

    if 'Bucaramanga' in equipo:
        equipo = 'Atletico Bucaramanga'
    elif 'Huila' in equipo:
        equipo = 'Atletico Huila'
    elif 'Rionegro' in equipo:
        equipo = 'Rionegro Aguilas Doradas'
    elif 'Nacional' in equipo:
        equipo = 'Atletico Nacional S.A'
    elif 'Medell' in equipo:
        equipo = 'Independiente Medellin'
    elif 'Boyac' in equipo:
        equipo = 'Boyaca Chico'
    elif 'Jaguares' in equipo:
        equipo = 'Jaguares de Cordoba'
    elif 'Magdalena' in equipo:
        equipo = 'Union Magdalena'
    elif 'rica de Cali' in equipo:
        equipo = 'America de Cali'
    elif 'Magdalena' in equipo:
        equipo = 'Union Magdalena'
    
    return equipo


browser = webdriver.Firefox()

browser.get("https://betplay.com.co/apuestas#filter/football/colombia/liga_betplay_dimayor")

time.sleep(10)
try:
    fechas = browser.find_elements(By.CLASS_NAME, 'CollapsibleContainer__LabelDetails-sc-14bpk80-8')
    lista_fechas = []
    for fecha in fechas:
        
        lista_fechas.append(fecha.text)
        break

    dia = browser.find_element(By.CLASS_NAME, 'CollapsibleContainer__CollapsibleWrapper-sc-14bpk80-0')

    lista_cuotas = []

    encuentros = dia.find_elements(By.CLASS_NAME, 'KambiBC-event-item__event-wrapper')

    for encuentro in encuentros:
        lista = []
        grupo_cuotas = encuentro.find_element(By.CLASS_NAME, 'KambiBC-bet-offers-list__column--num-3')
        cuotas = grupo_cuotas.find_elements(By.CLASS_NAME, 'sc-iBYQkv')
        for cuota in cuotas:
            lista.append(cuota.text)
        equipos_vs = encuentro.find_elements(By.CLASS_NAME, 'KambiBC-event-participants__name')
        for equipo in equipos_vs:
            lista.append(utf8_eq(equipo.text))
        lista.append(lista_fechas[0])
        lista_cuotas.append(lista)

    #print(lista_cuotas)

    browser.close()



    with open('./datos_consolidados.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel')
        csv_writer.writerows(lista_cuotas)
except:
    browser.close()