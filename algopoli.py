#!/usr/bin/python3
import features
from grafo import Grafo
from argparse import ArgumentParser

def generarGrafo(path):
    grafo = Grafo()
    with open(path, mode = 'r' ) as file:
        for line in file:
            verticeOrigen, verticeDestino = line.rstrip('\n').split('\t')
            grafo.agregar_vertice(verticeOrigen)
            grafo.agregar_vertice(verticeDestino)
            grafo.agregar_arista(verticeOrigen, verticeDestino)
    return grafo

def generarInstrucciones(path):
    comandos = []
    parametros = []
    with open(path, mode = 'r' ) as file:
        for linea in file:
            tempComando, tempParametros = linea.rstrip('\n').split(' ')
            comandos.append(tempComando)
            if tempParametros:
                parametros.append(tempParametros.split(','))
            else:
                parametros.append(None)

    return comandos, parametros

def main():
    '''
    '''
    parser = ArgumentParser( description='Argumentos de AlgoPoli' )
    parser.add_argument( 'grafoPath' , help='Directorio del archivo Generador del Grafo.' )
    parser.add_argument( '-comandosPath' , help='Directorio del archivo de comandos.')
    args = parser.parse_args()

    if args.comandosPath:
        comandos, parametros = generarInstrucciones(args.comandosPath)
    else:
        print()
        #esperar recibir comandos

    grafo = generarGrafo(args.grafoPath)
    print(grafo)
    
    #aplicar comandos
    
    return




main()