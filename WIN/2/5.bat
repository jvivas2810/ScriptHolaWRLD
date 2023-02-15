@echo off

set target_dir=C:\TEXTOS

if not exist %target_dir% (
mkdir %target_dir%
)

:loop
if "%1" == "" goto end_loop

echo Copiando %1 a %target_dir%
copy %1 %target_dir%

shift
goto loop

:end_loop
echo Copia completada.
pause