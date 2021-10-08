#!/usr/bin/env python
import sys

for line in sys.stdin:
    # Setea valores por defecto
	fecha = "-"
	palabra = ""
	cuentaDiaria = "-"
	cuentaTotal = "-"

	# Tratamiento de palabras desde entrada estandar
	line = line.strip()
	splits = line.split(" ")

	# Identifica cuentaDiaria, pues tiene mas columnas que cuentaTotal
	if len(splits) == 3:
		# Parsea registros
		fecha = splits[0]
		palabra = splits[1]
		cuentaDiaria = splits[2]
	# Identifica cuentaTotal
	else:
		# Parsea registros
		palabra = splits[0]
		cuentaTotal = splits[1]   
		
	# Escritura de los elementos (clave,valor) en salida estandar              
	print palabra + ' ' + fecha + ' ' + cuentaDiaria + ' ' + cuentaTotal