#!/usr/bin/env python
import sys
import string

last_palabra = None
cur_cuentaTotal = "-"

for line in sys.stdin:
    # Tratamiento de palabras desde entrada estandar
    line = line.strip()

    # Parseo de elementos (clave, valor) agrupados por clave
    palabra,fecha,cuentaDiaria,cuentaTotal = line.split(" ")

    # Identifica si es una nueva palabra
    if not last_palabra or last_palabra != palabra:
        last_palabra = palabra
        cur_cuentaTotal = cuentaTotal
    elif palabra == last_palabra:
        cuentaTotal = cur_cuentaTotal
        # Escritura del resultado en salida estandar
        print fecha + ' ' + palabra + ' ' + cuentaDiaria + ' ' + cuentaTotal