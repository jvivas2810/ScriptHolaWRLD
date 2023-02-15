@echo off
set file=%1
set option=%2

if "%option%" == "-o" (
  type %file% | sort | more
) else (
  type %file% | more
)

echo Tarea completada.
pause
