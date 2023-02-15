@echo off
set /p source_dir=Introduce la ruta del directorio origen:
if not exist %source_dir% (
echo Error: el directorio origen no existe.
pause
exit
)

set /p target_dir=Introduce la ruta del directorio destino (opcional):
if "%target_dir%" == "" set target_dir=C:\BACKUP

if not exist %target_dir% (
mkdir %target_dir%
)

for %%f in (%source_dir%*) do (
if exist %target_dir%%%~nxf (
echo Ya existe un archivo con el nombre %%~nxf en el directorio destino. ¿Desea reemplazarlo? [S/N]
set /p confirm=
if /i "%confirm%" == "S" (
copy /y %%f %target_dir%
)
) else (
copy %%f %target_dir%
)
)

echo Copia de seguridad completada.
pause