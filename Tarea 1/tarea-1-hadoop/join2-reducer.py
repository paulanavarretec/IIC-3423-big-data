#!/usr/bin/env python
import sys
import string

last_programa = None
audiencia_total = 0

for line in sys.stdin:
    # Tratamiento de palabras desde entrada estandar
    line = line.strip()

    # Parseo de elementos (clave, valor) agrupados por clave
    programa,audiencia = line.split(" ")
    audiencia = int(audiencia)

    # Identifica si es un programa antiguo
    if not last_programa or last_programa == programa:
        # Suma cantidad de audiencia
        audiencia_total += audiencia
        last_programa = programa
    # Identifica si es un programa nuevo
    elif programa != last_programa:
        # Escritura del resultado en salida estandar
        print last_programa + ' ' + str(audiencia_total)
        last_programa = programa
        audiencia_total = audiencia

# Escritura del ultimo programa
print last_programa + ' ' + str(audiencia_total)