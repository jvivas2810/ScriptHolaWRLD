import re
import csv
import subprocess
import chardet
import lxml
import urllib
from lxml import etree
from urllib import request

# URL del canal de Youtube
url = "https://www.youtube.com/@Andiamoyt/featured"

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

with open('videos.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    # Buscar la ID y el título de cada video en el código fuente
    for match in re.finditer(video_id_pattern, source_code): 
        video_id = match.group(1)
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        from pytube import YouTube
        yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
        video_title = yt.title
        print(video_title)

      
        writer.writerow([video_url, video_title])
        


