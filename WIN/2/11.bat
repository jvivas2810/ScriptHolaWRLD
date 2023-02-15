@echo off
if "%1" == "" (
echo Error: no se especificó unidad.
pause
exit
)

if "%2" == "" (
echo Error: no se especificó nombre de directorio.
pause
exit
)

if not exist "%1" (
echo Error: la unidad especificada no existe.
pause
exit
)

cd /d "%1"
if not exist "%2" (
mkdir "%2"
)

cd "%2"
if "%3" == "" (
echo Error: no se especificaron archivos para copiar.
pause
exit
)

for %%f in ("%3") do (
if not exist "%1"%%f (
echo Error: el archivo "%1"%%f no existe.
pause
exit
)
copy "%1"%%f .
)

echo Copia completada.
pause