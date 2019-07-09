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
                     

def main():
    '''
    '''
    parser = ArgumentParser( description='Argumentos AlgoPoli' )
    parser.add_argument( 'path' , help='Directorio del archivo Generador del Grafo.' )
    
    #parser.add_argument( 'commandos' , help='Directorio del archivo de comandos.')
    
    args = parser.parse_args()
    print(args.path)
    grafo = generarGrafo(args.path)
    print(grafo)



main()