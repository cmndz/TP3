import random
from grafo import * 
from collections import deque

factorDelRecorrido = 10

#-------------------------------------------------------------------#
#                           AUXILIARES                              #
#-------------------------------------------------------------------#
def caminoMinimo(grafo, origen):
    visitados = set()
    padre = {}
    distancia = {}
    queue = deque()
    #---------------------------------------------------------------
    padre[origen] = None
    distancia[origen] = 0
    queue.append(origen)
    #---------------------------------------------------------------
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
            vertice_origen = random.choice(list(grafo.adyacentes(vertice_origen)))	#Del vertice anterior se elije uno de sus adyacentes al azar
            vertices_apariciones[vertice_origen] += 1

            if i == (largo + iteraciones_extra - 1):
                iteraciones_extra = 0

    return vertices_apariciones

def countingSort(hash, MenorAMayor = True):
    minimo = min(list(hash.values()))
    maximo = max(list(hash.values()))
    rango = (maximo - minimo)+1
    #Calculo de Ocurrencias-----------------------------------------
    ocurrencias = []
    for i in range(rango):ocurrencias.insert(i,0)
    for i in hash.values(): ocurrencias[i-minimo] += 1
    #Sumas Parciales------------------------------------------------
    sumasParciales = []
    for i in range(rango+1):sumasParciales.insert(i,0)
    for i in range(rango): sumasParciales[i+1] = sumasParciales[i]+ocurrencias[i]
    #Solucion-------------------------------------------------------
    solucion = []
    for i in range(len(hash)):solucion.insert(i,None)
    for v in hash.keys():
        posicion = None
        if MenorAMayor: 
            posicion = sumasParciales[hash[v]-minimo]
        else:
            posicion = len(solucion)-sumasParciales[hash[v]-minimo]-1
        solucion[posicion] = v
        sumasParciales[hash[v]-minimo]+=1
    return solucion

def imprimirSeguimiento(padres, destino):
    stack = []
    vertice = destino
    #---------------------------------------------------------------
    while vertice:
        stack.append(vertice) 
        vertice = padres[vertice]
    #---------------------------------------------------------------
    while stack:
        print( stack.pop() , end = "" )
        if stack:
            print(" -> ", end = "")
            continue
        print()
    return

def primer_visita(grafo, labels, ady_para_cada_vertice):

    for v in grafo:
        labels[v] = random.randint(1, 1000)

        for w in grafo.adyacentes(v):

            if w == v:
                continue
            
            set_actual_de_adyacentes = ady_para_cada_vertice.get(w, set())
            ady_para_cada_vertice[w] = set_actual_de_adyacentes.add(v)

    return labels, ady_para_cada_vertice

def max_freq(grafo, adyacentes, labels):
    
    
    
    return 0

#-------------------------------------------------------------------#
#                         FUNCIONALIDADES                           #
#-------------------------------------------------------------------#
def min_seguimientos(grafo, origen, destino):
    '''Imprime el Camino Minimo entre un Vertice de Origen y uno de Destino, si es que fueran conexos.'''
    if not origen in grafo.vertices() or destino not in grafo.vertices():
        print("Seguimiento Imposible")
        return
    _, padres = caminoMinimo(grafo, origen)
    if destino not in padres.keys():
        print("Seguimiento Imposible")
        return

    imprimirSeguimiento(padres, destino)
    return

def mas_imp(grafo, cant):
    '''Imprime los Vertices de mayor a menor centralidad dentro del grafo'''
    cant_recorridos = grafo.cantidad_vertices()#*factorDelRecorrido
    largo = grafo.cantidad_vertices()#*factorDelRecorrido

    vertices_apariciones = random_walks(grafo, largo, cant_recorridos)
    
    verticesOrdPorCentralidad = countingSort(vertices_apariciones, False)
    
    for i in range(cant):
        print(verticesOrdPorCentralidad[i], end = "")
        if i+1 < cant: 
            print(", ", end = "")
            continue
        print()

    return 

def persecucion(grafo, verticesDeOrigen, k):
    '''Imprime el Camino Minimo entre un Vertices de Origen y uno de los Vertices con mayor Centralidad'''
    cant_recorridos = grafo.cantidad_vertices()#*factorDelRecorrido
    largo = grafo.cantidad_vertices()#*factorDelRecorrido
    vertices_apariciones = random_walks(grafo, largo, cant_recorridos)
    verticesOrdPorCentralidad = countingSort(vertices_apariciones, False)
            
    distancia_aux = 0
    destinoFinal = None
    padresFinal = None

    for origen in verticesDeOrigen:
        distancias, padres = caminoMinimo(grafo, origen)
        for destino in verticesOrdPorCentralidad:
            if origen == destino: continue
            if not destinoFinal == None:
                if distancias[destino] > distancia_aux or (distancias[destino] == distancia_aux and 
                    verticesOrdPorCentralidad.index(destino) > verticesOrdPorCentralidad.index(destinoFinal)):
                    continue
            distancia_aux = distancias[destino]
            destinoFinal = destino
            padresFinal = padres

    imprimirSeguimiento(padresFinal, destinoFinal )
    return

def comunidades(grafo, n):
    '''Imprime un listado de Comunidades de al menos n integrantes'''
    labels = {}
    ady_para_cada_vertice = {}

    labels, ady_para_cada_vertice = primer_visita(grafo, labels, ady_para_cada_vertice)

    for _ in range(0, 50):

        for v in grafo:
            
            labels[v] = max_freq(grafo, ady_para_cada_vertice[v], labels)





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