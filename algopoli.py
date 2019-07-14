#!/usr/bin/python3
from features import (min_seguimientos, mas_imp,
persecucion, comunidades, divulgar, divulgar_ciclo, cfc)
from grafo import Grafo
from argparse import ArgumentParser
from sys import stdin

def generarGrafo(path):
	'''
	Genera un Grafo mediante un archivo .tsv 
	indicado en el parametro path.
	'''
	grafo = Grafo()
	with open(path, mode = 'r' ) as file:
		for line in file:
			verticeOrigen, verticeDestino = line.rstrip('\n').split('\t')
			grafo.agregar_vertice(verticeOrigen)
			grafo.agregar_vertice(verticeDestino)
			grafo.agregar_arista(verticeOrigen, verticeDestino)
	return grafo

def interpretarComando(grafo, line):
	'''
	Intepreta la linea recibida, y ejecuta 
	el comando correspondiente sobre el grafo.
	'''
	comandos = { 
		'min_seguimientos':1
		, 'mas_imp':2
		, 'persecucion':3
		, 'comunidades':4
		, 'divulgar':5
		, 'divulgar_ciclo':6
		, 'cfc':7
	}
	comando = None
	parametros = None

	listLine = line.rstrip('\n').split(' ') 

	if len(listLine)>1:
		parametros = listLine[1:]
		if ',' in parametros[0]:
			temp = parametros[0].split(',')
			parametros[0] = temp

	comando = comandos[listLine[0]]

	if comando == 1: min_seguimientos(grafo, parametros[0], parametros[1])
	elif comando == 2: mas_imp(grafo, int(parametros[0]))
	elif comando == 3: persecucion(grafo, parametros[0], int(parametros[1]))
	elif comando == 4: comunidades(grafo, int(parametros[0]))
	elif comando == 5: divulgar(grafo, parametros[0], int(parametros[1]))
	elif comando == 6: divulgar_ciclo(grafo, parametros[0], int(parametros[1]))
	else: cfc(grafo)
	return 

def main():
	'''
	Funcion Principal.
	'''
	parser = ArgumentParser( description='Argumentos de AlgoPoli' )
	parser.add_argument( 'grafoPath' , help='Directorio del archivo Generador del Grafo.' )
	args = parser.parse_args()
	grafo = generarGrafo(args.grafoPath)
	for line in stdin: interpretarComando(grafo, line)
	return

main()