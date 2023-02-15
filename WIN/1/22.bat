@echo off
setlocal EnableDelayedExpansion

set /p caracteres = Introduzca una cadena:
set /p directorio=Introduzca un directorio:
set /a contador=0

if exist ficheros.txt (
    del ficheros.txt
)

for /r %%a in (%directorio%\%caracteres%*) do (
    if "!contador!" == "0" (
       echo %%a >> ficheros.txt
)

if exist ficheros.txt (
    type ficheros.txt
) else (
    echo No han sido encontrados archivos con %caracteres% en el nombre
)