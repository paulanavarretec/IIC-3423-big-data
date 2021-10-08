#!/usr/bin/env python
import sys

for line in sys.stdin:
    # Tratamiento de palabras desde entrada estandar
    line = line.strip()
    words = line.split()
    for word in words:
        # Escritura de los elementos (clave,valor) en salida estandar
        print '%s\t%s' % (word, 1)