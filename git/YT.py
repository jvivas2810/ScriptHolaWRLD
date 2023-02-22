import re
import csv
import subprocess
import chardet
import requests
from bs4 import BeautifulSoup

# URL del canal de Youtube
url = "https://www.youtube.com/@OfficialJaden/featured"

# Comando para obtener el código fuente con curl
# Obtiene el código fuente con curl
command = 'curl --silent --location "{}" > source_code.txt'.format(url)
output = subprocess.check_output(command, shell=True)

# Lee el contenido del archivo y decodifica la codificación
with open('source_code.txt', 'rb') as f:
    rawdata = f.read()
    result = chardet.detect(rawdata)
    source_code = rawdata.decode(result['encoding'])

# Patrón para buscar la ID de un video en la URL del video
video_id_pattern = re.compile(r'/watch\?v=([^\s&]+)","webPageType":"WEB_PAGE_TYPE_WATCH"')

# Patrón para buscar el título del video en el código fuente
# Patrón para buscar el título del video en el código fuente
video_title_pattern = re.compile(r'"title":{"accessibility":{"accessibilityData":{"label":"(.*?) hace \d+ días \d+ horas \d+ minutos y \d+ segundos [\d.]+ visualizaciones"}},"simpleText":"([^"]+)"')

# Conjunto para mantener un registro de títulos únicos
unique_titles = set()

with open('videos.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    # Buscar la ID y el título de cada video en el código fuente
    for match in re.finditer(video_id_pattern, source_code): 
        video_id = match.group(1)
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        
        # Leer el contenido del archivo de código fuente y buscar el título
        # Hacer una petición GET al URL del video
        response = requests.get(video_url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Aquí busca el contenido en la etiqueta <title>
        video_title = soup.find("title").get_text()

        # Verificar si el título ya está en el conjunto de títulos únicos
        if video_title not in unique_titles:
            # Agregar el título al conjunto de títulos únicos
            unique_titles.add(video_title)
            writer.writerow([video_url, video_title])
            print(video_title)









