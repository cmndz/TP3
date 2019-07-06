from grafo import * 
from collections import deque

#-------------------------------------------------------------------#
#                           AUXILIARES                              #
#-------------------------------------------------------------------#
def caminoMinimo(grafo, origen):
    visitados = set()
    padre = {}
    distancia = {}
    queue = deque()
    #-----
    padre[origen] = None
    distancia[origen] = 0
    queue.append(origen)
    #-----
    while queue:
        v = queue.popleft()
        visitados.add(v)
        for w in grafo.adyacentes(v):
            if not w in visitados:
                padre[w] = v
                distancia[w] = distancia[v]+1
                queue.append(w)
    return distancia, padre

#def randomWalks(grafo, origen, pasos):


'''
def calcularCentralidad( grafo ):
    centralidad = {}
    for v in grafo.vertices(): centralidad[v] = 0
    for v in grafo.vertices():
        
        #distancia, padre = caminoMinimo(grafo,v)
        aux = {}
        for w in grafo.vertices():aux[w] = 0
        #vertices_ordenados = ordenar_vertices(grafo, distancias)



        
        

    return centralidad
'''

#-------------------------------------------------------------------#
#                         FUNCIONALIDADES                           #
#-------------------------------------------------------------------#
def min_seguimientos(grafo, origen, destino):
    '''Imprime el Camino Minimo entre un Vertice de Origen y uno de Destino, si es que fueran conexos.'''
    if not origen in grafo.vertices() or destino not in grafo.vertices():   #Nos aseguramos que ambos 
        print("Seguimiento Imposible")                                      #vertices se encuetren en el Grafo.
        return
    _, padre = caminoMinimo(grafo, origen)
    if destino not in padre.keys():                                                  #Nos aseguramos de que ambos 
        print("Seguimiento Imposible")                                      #vertices esten en la misma 
        return                                                              #componente conexa.
    stack = []
    v = destino
    while v:                                                                #Apilamos los vertices,
        stack.append(v)                                                     #desde el Destino, 
        v = padre[v]                                                        #hacia el Origen.

    while stack:                                                            #Desapilamos, mientras
        print( stack.pop() , end = "" )                                     #imprimimos el seguimiento.
        if stack:
            print(" -> ", end = "")
            continue
        print()
    return

def mas_imp(grafo, cant):
    '''Imprime los Vertices de mayor a menor centralidad dentro del grafo'''
    #centralidad = calcularCentralidad( grafo ):








#def persecucion():

g = Grafo()
print(g)

print("Agrego A",g.agregar_vertice('A'))
print("Agrego B",g.agregar_vertice('B'))
print("Agrego C",g.agregar_vertice('C'))
print("Agrego D",g.agregar_vertice('D'))
print("Agrego E",g.agregar_vertice('E'))
print("Agrego F",g.agregar_vertice('F'))

print("Agrego AB",g.agregar_arista('A','B'))
print("Agrego BC",g.agregar_arista('B','C'))
print("Agrego CD",g.agregar_arista('C','D'))
print("Agrego AE",g.agregar_arista('A','E'))
print("Agrego BF",g.agregar_arista('B','F'))
print("Agrego DF",g.agregar_arista('D','F'))
print("Agrego DF",g.agregar_arista('D','F'))
print("Agrego DF",g.agregar_arista('D','F'))
print(g)
#print('Adyacentes de A',g.adyacentes('A'))
min_seguimientos(g, 'A', 'F')
print("Remuevo DF",g.borrar_arista('B','F'))
print(g)
min_seguimientos(g, 'A', 'F')
print("Remuevo B", g.borrar_vertice('B'))
min_seguimientos(g, 'A', 'F')
#g.verticeRemover('A')
#g.verticeRemover('B')
#print(g.vertices())
#print(g.)