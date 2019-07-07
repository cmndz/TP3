import random
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

def random_walks(grafo, largo, cant_recorridos):
    vertices_apariciones = {}
    
    for v in grafo: 
        vertices_apariciones[v] = 0
    
    for _ in range (0, cant_recorridos):	#Para una cantidad de recorridos
        
        vertice_origen = grafo.vertice_random()
        vertices_apariciones[vertice_origen] += 1

        iteraciones_extra = 0

        for i in range (0, largo + iteraciones_extra):	#Para una cantidad "largo" de veces
            
            if not grafo.adyacentes(vertice_origen):
                iteraciones_extra = largo - i
                continue
            vertice_random = random.choice(list(grafo.adyacentes(vertice_origen)))	#Del vertice anterior se elije uno de sus adyacentes al azar
            vertices_apariciones[vertice_random] += 1

            if i == (largo + iteraciones_extra - 1):
                iteraciones_extra = 0

    return vertices_apariciones

#-------------------------------------------------------------------#
#                         FUNCIONALIDADES                           #
#-------------------------------------------------------------------#
def min_seguimientos(grafo, origen, destino):
    '''Imprime el Camino Minimo entre un Vertice de Origen y uno de Destino, si es que fueran conexos.'''
    if not origen in grafo.vertices() or destino not in grafo.vertices():   #Nos aseguramos que ambos 
        print("Seguimiento Imposible")                                      #vertices se encuetren en el Grafo.
        return
    _, padre = caminoMinimo(grafo, origen)
    if destino not in padre.keys():                                         #Nos aseguramos de que ambos 
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
    cant_recorridos = grafo.cantidad_vertices()*10
    largo = grafo.cantidad_vertices()*10

    vertices_apariciones = random_walks(grafo, largo, cant_recorridos)

    for _ in range(cant):
        valor = 0
        clave = None
        for v in vertices_apariciones.keys():
            if vertices_apariciones[v] > valor:
                valor = vertices_apariciones[v]
                clave = v
        vertices_apariciones.pop(clave)  
        print(clave)
    return

def persecucion(grafo, delincuenteN, k):
    cant_recorridos = grafo.cantidad_vertices()*10
    largo = grafo.cantidad_vertices()*10

    vertices_apariciones = random_walks(grafo, largo, cant_recorridos)
    vertices_importantes = []
    
    for _ in range(k):
        valor = 0
        clave = None
        for v in vertices_apariciones.keys():
            if vertices_apariciones[v] > valor:
                valor = vertices_apariciones[v]
                clave = v
        vertices_apariciones.pop(clave)
        vertices_importantes.append(clave)
        
    distancia_aux = 0
    vertice_aux = None
    padre_aux = None
    distancia_aux = None
    for d in delincuenteN:
        distancia, padre = caminoMinimo(grafo, d)
        for c in vertices_importantes:
            if distancia[c] > distancia_aux: continue
            if distancia[c] == distancia_aux and vertices_importantes.index(c)> vertices_importantes.index(vertice_aux): continue
            distancia_aux = 0
            vertice_aux = c
            padre_aux = padre
            distancia_aux = distancia

    stack = []
    v = vertice_aux
    while v:                                                                #Apilamos los vertices,
        stack.append(v)                                                     #desde el Destino, 
        v = padre_aux[v]                                                        #hacia el Origen.

    while stack:                                                            #Desapilamos, mientras
        print( stack.pop() , end = "" )                                     #imprimimos el seguimiento.
        if stack:
            print(" -> ", end = "")
            continue
        print()




    return






    
    

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

mas_imp(g, 2)


#print(g.vertice_random())
'''
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
#print(g.)'''