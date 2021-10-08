#!/usr/bin/env python
import sys

for line in sys.stdin:
    # Setea valores por defecto
	programa = ""
	audiencia = "0"
	canal = False

	# Tratamiento de palabras desde entrada estandar
	line = line.strip()
	splits = line.split(",")

	# Se reconoce si segundo campo es un digito (programa,audiencia)
	if splits[1].isdigit():
		programa = splits[0]
		audiencia = splits[1]
		canal = True 
	# Se reconoce (programa,canal)
	else:
		programa = splits[0]
		canal = splits[1]=='CAB'
	# Chequea si canal = CAB
	if canal:
		# Escritura de los elementos (clave,valor) en salida estandar
		print programa + ' ' + audiencia