#Jorge Vivas Díaz   2ºAsir B
#-----------------------------------------
#Archivo csv con nombre y url de peliculas
#Importamos los modulos necesarios
import requests
from bs4 import BeautifulSoup
import csv

#Definimos la url de la cartelera de elpais
url = "https://cartelera.elpais.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

#Buscamos los elementos con la clase movie y extraemos el titulo y la url
movies = []
for movie in soup.find_all("li", {"class": "movie"}):
    title = movie.find("a").attrs["title"]
    link = movie.find("a").attrs["href"]
    movies.append({"title": title, "link": link})

#Escribimos todo en un archivo csv
with open("cartel.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["NOMBRE DE LA PELICULA", "URL DEL CARTEL"])
    for movie in movies:
        writer.writerow([movie["title"], movie["link"]])
        print (movie["title"])

#Para exportar el archivo por ftp
#Importamos los modulos necesarios
import ftplib
import os
import ssl

#Definimos los datos de cada una de las cuentas de los clientes
ftp_account1 = {
    "host": "192.168.206.154",
    "user": "Kinepolis",
    "password": "Kinepolis",
}

ftp_account2 = {
    "host": "192.168.206.154",
    "user": "YelmoCines",
    "password": "YelmoCines",
}

#Establecemos la conexión con cada cuenta
def secure_ftp_connect(account):
    ftp = ftplib.FTP_TLS(account["host"])
    ftp.login(account["user"], account["password"])
    ftp.prot_p()
    return ftp

ftp1 = secure_ftp_connect(ftp_account1)
ftp2 = secure_ftp_connect(ftp_account2)

#Cargamos el archivo csv en cada cuenta
filename = "cartel.csv"

with open(filename, "rb") as file:
    # Cargar en cuenta FTP 1
    ftp1.cwd("/")
    ftp1.storbinary("STOR " + os.path.basename(filename), file)

    # Cargar en cuenta FTP 2
    ftp2.cwd("/")
    ftp2.storbinary("STOR " + os.path.basename(filename), file)

print("Archivo cargado en ambas cuentas FTP")

#cerramos la conexion
ftp1.quit()
ftp2.quit()

