#!/usr/bin/env python
from operator import itemgetter
import sys

cur_word = None
cur_count = 0
word = None

for line in sys.stdin:
    # Tratamiento de palabras desde entrada estandar
    line = line.strip()

    # Parseo de elementos (clave, valor) agrupados por clave
    word, count = line.split('\t', 1)

    # Convierte contador a entero
    try:
        count = int(count)
    except ValueError:
        continue

    # Suma de ocurrencias
    if cur_word == word:
        cur_count += count
    else:
        if cur_word:
            # Escritura del resultado en salida estandar
            print '%s\t%s' % (cur_word, cur_count)
        cur_count = count
        cur_word = word

# Escritura del ultimo valor en salida estandar
if cur_word == word:
    print '%s\t%s' % (cur_word, cur_count)