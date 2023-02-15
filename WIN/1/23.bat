@echo off
setlocal EnableDelayedExpansion

:inicio
echo 1. Conectar un recurso compartido
echo 2. Ver recursos compartidos disponibles
echo 3. Borrar un recurso compartido
echo 4. Salir

set /p opcion="Eliga una opcion: "

if "%opcion%" == "" echo necesita coger una opcion


if "%opcion%" == "1" goto opcion1
if "%opcion%" == "2" goto opcion2
if "%opcion%" == "3" goto opcion3
if "%opcion%" == "4" goto opcion4

:opcion1 
set /p unidad= "Indica la letra: "

:opcion2
net share
pause
goto inicio

:opcion3 
set /p unidad3= Indica la letra de unidad
net use %unidad3%: /delete
pause
goto inicio

:opcion4
exit