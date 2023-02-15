@echo off

set archivo=%1

for /F "usebackq tokens=1,2 delims=," %%a in ("%archivo%") do (
    set nombre=%%a
    set clave=%%b
    echo "%%a"
    echo "%%b"

    net user %nombre% %clave% /add
)