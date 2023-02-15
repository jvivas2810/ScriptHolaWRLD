@echo off
set /p string=Introduce la cadena a buscar: 
set /p source_dir=Introduce la ruta
set target_dir=C:\COPIA\

if not exist C:\COPIA\ (
    mkdir C:\COPIA
)

for %%f in (%source_dir%\*) do (
  find "%string%" %%f > nul
  if not errorlevel 1 (
    echo Copying %%f to %target_dir%
    copy %%f %target_dir%
  )
)

echo Busqueda completada.
pause
