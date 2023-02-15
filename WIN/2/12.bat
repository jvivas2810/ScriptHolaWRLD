@echo off
set target_dir=%1
shift

for %%d in (%*) do (
  xcopy /s /i "%%d" %target_dir%
  if not errorlevel 1 (
    echo Copia de "%%d" a %target_dir% realizada con éxito.
    rmdir /s /q "%%d"
  ) else (
    echo Error al copiar "%%d" a %target_dir%.
  )
)

echo Tarea completada.
pause
