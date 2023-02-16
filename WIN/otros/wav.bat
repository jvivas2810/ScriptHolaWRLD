@echo off
setlocal EnableDelayedExpansion
if not exist mp3folder mkdir mp3folder

rem Creamos un bucle for para recorrer todos los archivos

:ask_bitrate
set /p bitrate=Introduce la tasa de bits en kbps:

rem Comprobamos si la tasa de bits es nula
if "%bitrate%"=="" (
    echo No has introducido ninguna tasa de bits. Inténtalo de nuevo.
    goto ask_bitrate
)

rem Comprobamos si la tasa de bits es una no permitida (menor que 128 o mayor que 320)
if %bitrate% LSS 128 (
    echo La tasa de bits debe ser mayor o igual a 128 kbps. Inténtalo de nuevo.
    goto ask_bitrate
)

if %bitrate% GTR 320 (
    echo La tasa de bits debe ser menor o igual a 320 kbps. Inténtalo de nuevo.
    goto ask_bitrate
)

rem Continuamos con el resto del script
for %%f in (*.wav) do (
    echo %%~nf
    set name=%%~nf
    C:\Users\Usuario\Downloads\ffmpeg-2023-02-13-git-2296078397-full_build\ffmpeg-2023-02-13-git-2296078397-full_build\bin\ffmpeg.exe -i "%%f" -b:a %bitrate%k -q:a 0 "!name!.mp3"
    move "!name!.mp3" mp3folder
)