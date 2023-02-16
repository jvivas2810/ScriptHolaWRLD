@echo off
setlocal EnableDelayedExpansion
if not exist mp4folder mkdir mp4folder

for %%f in (*.vob) do (
    echo %%~nf
    set name=%%~nf
    C:\Users\Usuario\Downloads\ffmpeg-2023-02-13-git-2296078397-full_build\ffmpeg-2023-02-13-git-2296078397-full_build\bin\ffmpeg.exe -i "%%f" "!name!.mp4"
    move "!name!.mp4" mp4folder
)