import random
from grafo import * 
from collections import deque

#-------------------------------------------------------------------#
#                           AUXILIARES                              #
#-------------------------------------------------------------------#
def caminoMinimo(grafo, origen, distanciaMax = None):
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
                if distanciaMax and distancia[v] == distanciaMax:
                    return distancia, padre
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

def imprimirListado(lista, limite = None):
    if not limite: limite = len(lista)
    #---------------------------------------------------------------
    for i in range(0, limite):
        print(lista[i], end = "")
        if i+1 < limite: 
            print(", ", end = "")
            continue
        print()
    return

def asignar_labels(grafo, labels, ady_para_cada_vertice):

	for v in grafo:
		labels[v] = random.randint(1, 1000)

		for w in grafo.adyacentes(v):

			if w == v:
				continue

			set_actual_de_adys = ady_para_cada_vertice.get(w, set())
			ady_para_cada_vertice[w] = set_actual_de_adys.add(v)

	return labels, ady_para_cada_vertice


def max_freq(vertice, adyacentes, labels):

	if not adyacentes:
		return labels[vertice]

	frecuencias = {}
	max_act = 0

	for v in adyacentes:

		numero_id = labels[v]
		contador = frecuencias.get(numero_id, 0) + 1
		frecuencias[numero_id] = contador

		if frecuencias[numero_id] > max_act:
			max_act = frecuencias[numero_id]
			label_actual = numero_id

	return label_actual


def impresion_de_comunidades(dict_comunidades, n):

	comunidad_impresa = 1

	for comunidad in dict_comunidades:

		cant_integrantes = len(dict_comunidades[comunidad])

		if cant_integrantes >= n:

			print("Comunidad {}: ".format(comunidad_impresa))
			comunidad_impresa += 1

			integrante_impreso = 1

			for integrante in dict_comunidades[comunidad]:
				print(integrante)

				if integrante_impreso != cant_integrantes:
					print(", ")

				integrante_impreso += 1

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
    cant_recorridos = grafo.cantidad_vertices()
    largo = grafo.cantidad_vertices()

    vertices_apariciones = random_walks(grafo, largo, cant_recorridos)
    
    verticesOrdPorCentralidad = countingSort(vertices_apariciones, False)
    
    imprimirListado(verticesOrdPorCentralidad, cant)
    return 

def persecucion(grafo, verticesDeOrigen, k):
    '''Imprime el Camino Minimo entre un Vertices de Origen y uno de los k Vertices con mayor Centralidad'''
    cant_recorridos = grafo.cantidad_vertices()
    largo = grafo.cantidad_vertices()
    vertices_apariciones = random_walks(grafo, largo, cant_recorridos)
    verticesOrdPorCentralidad = countingSort(vertices_apariciones, False)
            
    distancia_aux = 0
    destinoFinal = None
    padresFinal = None

    for origen in verticesDeOrigen:
        distancias, padres = caminoMinimo(grafo, origen)
        for i in range(k):
            destino = verticesOrdPorCentralidad[i]
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
    '''Imprime un listado de comunidades de al menos n integrantes.'''
    labels = {}
    ady_para_cada_vertice = {}
    dict_comunidades = {}

    labels, ady_para_cada_vertice = asignar_labels(grafo, labels, ady_para_cada_vertice)

    iteraciones = 50	#numero al azar para testear con los tiempos este se puede cambiar para bajar los tiempos

    for i in range(0 , iteraciones):

        for v in grafo:
		
            labels[v] = max_freq(v, ady_para_cada_vertice[v], labels)

            if (i == iteraciones - 1):
                integrantes = dict_comunidades.get(labels[v], set())
                dict_comunidades[labels[v]] = integrantes.add(v)

    impresion_de_comunidades(dict_comunidades, n)

def divulgar(grafo, origen, n):
    '''Imprime todos los Vertices a una distancia n o menor, al Vertice de Origen'''
    distancias, _ = caminoMinimo(grafo,origen,n)
    lista = []
    for vertice in distancias.keys():
        if vertice == origen: continue
        lista.append(vertice)
    imprimirListado(lista)
    return



g = Grafo()
print(g)

g.agregar_vertice('A')
g.agregar_vertice('B')
g.agregar_vertice('C')
g.agregar_vertice('D')
g.agregar_vertice('E')
g.agregar_vertice('F')
g.agregar_arista('A','B')
g.agregar_arista('B','C')
g.agregar_arista('C','D')
g.agregar_arista('A','E')
g.agregar_arista('B','F')
g.agregar_arista('D','F')
g.agregar_arista('D','F')
g.agregar_arista('D','F')
print(g)

print("Mas Imp!")
mas_imp(g, 2)
print("Divulgar")
divulgar(g, 'A', 1)
divulgar(g, 'A', 2)
print("Persecucion")
lista = ['A','B']
persecucion(g,lista,1)
print("Comunidades")
comunidades(g, 2)


