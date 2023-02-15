#!/bin/bash

if [ ! -d $1 ] ; then
    echo "Debes espicificar un directorio como primer parametro"

fi

ficheros=0
directorios=0
tfichero=0
tdirectorio=0

for i in $*
do
    if  [ -d $i ];then                
        echo $i
        $directorios=$directorios+1
        $tdirectorio=$tdirectorio + wc -c
    elif [ -f $i ];then
        $ficheros=$ficheros+1
        $tfichero=$tfichero + wc -c
    fi

echo $directorios
echo $ficheros

echo $tdirectorio/$directorios
echo $tfichero/$ficheros