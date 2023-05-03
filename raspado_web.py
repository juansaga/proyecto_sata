from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from datetime import datetime 

 

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

# browser es la instancia de wedriver que permite interactuar con la web
# se usa el navegador Firefox
browser = webdriver.Firefox()
browser.implicitly_wait(60)
browser.get("https://betplay.com.co/apuestas#filter/football/colombia/liga_betplay_dimayor")
browser.implicitly_wait(60)

# las siguientes variables guardan la información que necesito,
# en formato de html
cuotas_html = browser.find_elements(By.CLASS_NAME,"sc-iBYQkv")
equipos_html = browser.find_elements(By.CLASS_NAME,"KambiBC-event-participants__name")

# en estas listas se almacena la informacion en el formato adecuado: str y float
# obtenidos de los formatos html
cuotas = []
equipos = []

for cuota in cuotas_html:
    cuotas.append(utf8_eq(cuota.text))
    
for equipo in equipos_html:
    equipos.append(utf8_eq(equipo.text))

# descomanetar esta línea muestra las cuotas y los equipos que juegan 
# print(cuotas, equipos)

# a continucion, organizamos los datos para almacenar en la base de datos
cantidad_partidos_segun_cuotas = int(len(cuotas)/5)
cantidad_partidos_segun_equipos = int(len(equipos)/2)
BD = []
now = datetime.now()
try:
    for i in range(0,cantidad_partidos_segun_cuotas):
        elemento = cuotas[ 5*i : 5*(i+1)] + equipos[ 2*i : 2*(i+1) ] + [now.strftime('%Y-%m-%d')]
        BD.append(elemento) 
except:
    print('la cantidad de cuotas no corresponde con la cantidad de partidos')


# print(BD)
browser.close()
with open('./pre_base.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(BD)
