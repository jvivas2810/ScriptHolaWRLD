if "%guia%" == "SI" (
    echo "Mostrando la guia de atributos"
    attrib /? | more
) else (
    echo "Has elegido no ver la guia"
)

set /p atributos="Indica los atributos"
attrib %atributos% %archivo%
echo "Se ha modificado el archivo %archivo% con los artributos %atributos%"
attrib %archivo%


