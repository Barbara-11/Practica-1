from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://mexico.as.com/resultados/futbol/mexico_apertura/clasificacion/"
page= requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")

#Equipos

eq=soup.find_all("span", class_="nombre-equipo")

equipos=list()

count=0
for i in eq:
    if count<20:
        equipos.append(i.text)
    else:
        break
    count+=1
print(eq)
print("\n")

#Puntos

pt=soup.find_all("td", class_="destacado")

puntos=list()

count=0
for i in pt:
    if count<20:
        puntos.append(i.text)
    else:
        break
    count+=1
print(pt)
print("\n")

df=pd.DataFrame({'Nombre':equipos,'Puntos':puntos},index=list(range(1,21)))

df.to_csv("Clasificacion.csv",index=False)

print("Lo que se guarda en el excel es:\n")
print(df)
