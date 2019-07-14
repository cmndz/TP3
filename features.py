from random import choice
from grafo import Grafo
from collections import deque

#-------------------------------------------------------------------#
#                           AUXILIARES                              #
#-------------------------------------------------------------------#
def caminoMinimo(grafo, origen, distanciaMax = None):
	'''
	Realiza un recorrido, en amplitud, por el Grafo paasado por parametro,
	a partir de un Vertice de Origen.
	
	Opcionalmente, tiene tercer parametro para indicar la distancia 
	maxima hasta la cual recorrer el Grafo.
	'''
	visitados = set()
	padre = {}
	distancia = {}
	queue = deque()

	visitados.add(origen)
	padre[origen] = None
	distancia[origen] = 0
	queue.append(origen)

	while queue:
		v = queue.popleft()
		for w in grafo.adyacentes(v):
			if not w in visitados:
				if distanciaMax and distancia[v] == distanciaMax:
					return distancia, padre
				visitados.add(w)
				padre[w] = v
				distancia[w] = distancia[v]+1
				queue.append(w)
	return distancia, padre

def random_walks(grafo, largo, cant_recorridos):
	'''
	Aplica el algoritmo de RandomWalks para obtener una 
	aproximacion a la importancia de cada Vertice dentro del Grafo.

	Ademas del Grafo sobre el cual operar, se le debe indicar 
	la Cantidad de Recorridos a realizar, y el Largo de cada uno.
	'''
	vertices_apariciones = {}
	
	for v in grafo: 
		vertices_apariciones[v] = 0
	
	for _ in range (0, cant_recorridos):
		
		vertice_origen = grafo.vertice_random()
		vertices_apariciones[vertice_origen] += 1
		iteraciones_extra = 0

		for i in range (0, largo + iteraciones_extra):
			
			if not grafo.adyacentes(vertice_origen):
				iteraciones_extra = largo - i
				continue
			vertice_origen = choice(list(grafo.adyacentes(vertice_origen)))
			vertices_apariciones[vertice_origen] += 1

			if i == (largo + iteraciones_extra - 1):
				iteraciones_extra = 0

	return vertices_apariciones

def countingSort(hash, MenorAMayor = True):
	'''
	Aplica Counting Sort para devolver una lista con las 
	Claves de un Diccionario, ordenados por los Valores de cada Clave.

	Opcionalmente, contiene un segundo parametro, para indicar si el 
	Ordenamiento debe hacerse de Menor a Mayor, o a la inversa.
	'''
	minimo = min(list(hash.values()))
	maximo = max(list(hash.values()))
	rango = (maximo - minimo)+1

	ocurrencias = []
	for i in range(rango): ocurrencias.insert(i,0)
	for i in hash.values(): ocurrencias[i-minimo] += 1

	sumasParciales = []
	for i in range(rango+1): sumasParciales.insert(i,0)
	for i in range(rango): sumasParciales[i+1] = sumasParciales[i]+ocurrencias[i]

	solucion = []
	for i in range(len(hash)): solucion.insert(i,None)
	for v in hash.keys():
		posicion = None
		if MenorAMayor: 
			posicion = sumasParciales[hash[v]-minimo]
		else:
			posicion = len(solucion)-sumasParciales[hash[v]-minimo]-1
		solucion[posicion] = v
		sumasParciales[hash[v]-minimo]+=1
	return solucion

def asignar_labels(grafo):
	'''
	Se encarga de asignar un label a cada Vertice del Grafo
	y calcular, para cada Vertice, los Vertices de Entrada al mismo.
	'''
	labels = {}
	ady_para_cada_vertice = {}
	id_vertice = 1

	for v in grafo:

		labels[v] = id_vertice
		id_vertice += 1

		if v not in ady_para_cada_vertice:
			adys_de_v = set()
			ady_para_cada_vertice[v] = adys_de_v

		for w in grafo.adyacentes(v):

			if w == v:
				continue

			set_actual_de_adys = ady_para_cada_vertice.get(w, set())
			set_actual_de_adys.add(v)
			ady_para_cada_vertice[w] = set_actual_de_adys

	return labels, ady_para_cada_vertice

def max_freq(vertice, adyacentes, labels):
	'''
	Devuelve el label con mayor cantidad de ocurrencias.
	entre los adyacentes de un Vertice.
	'''
	if len(adyacentes) == 0:
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

def encontrar_ciclo(grafo, vertice_orig, vertice_act, pasos, vertices_usados):
	'''
	Funcionamiento interno de la funcion divulgar_ciclo.
	Devuelve una lista con los Vertices que componen el Ciclo 
	en la cantidad de pasos solicitados, si es que existe, sino None.
	'''
	if (pasos == 0 and vertice_act != vertice_orig):
		return None

	if (pasos == 0 and vertice_act == vertice_orig):
		vertices_en_ciclo = []
		return vertices_en_ciclo

	vertices_usados.add(vertice_act)

	for w in grafo.adyacentes(vertice_act):

		if (w != vertice_orig and w in vertices_usados):
			continue

		if (w == vertice_orig and pasos != 1):
			continue

		vertices_en_ciclo = encontrar_ciclo(grafo, vertice_orig, w, pasos - 1, vertices_usados)

		if vertices_en_ciclo != None:

			vertices_en_ciclo.append(w)
			return vertices_en_ciclo

	vertices_usados.remove(vertice_act)
	return None

def _cfc(grafo, verticeOrigen, visitados, orden, stack1, stack2, cfcs, en_cfcs):
	'''
	Funcionamiento interno para calcular las 
	Componentes Fuertemente Conexas.
	'''
	visitados.add(verticeOrigen)
	stack1.append(verticeOrigen)
	stack2.append(verticeOrigen)
	for verticeAdy in grafo.adyacentes(verticeOrigen):
		if verticeAdy not in visitados:
			orden[verticeAdy] = orden[verticeOrigen]+1
			_cfc(grafo, verticeAdy, visitados, orden, stack1, stack2, cfcs, en_cfcs)
		elif verticeAdy not in en_cfcs:
			while orden[stack1[-1]] > orden[verticeAdy]:
				stack1.pop()

	if stack1[-1] == verticeOrigen:
		stack1.pop()
		verticeAux = None
		nueva_cfc = []
		while not verticeAux == verticeOrigen:
			verticeAux = stack2.pop()
			en_cfcs.add(verticeAux)
			nueva_cfc.append(verticeAux)
		cfcs.append(nueva_cfc)

def imprimirSeguimiento(padres, destino = None):
	'''
	Se encarga de Imprimir el resultado de las funciones
	que requieran un formato de "Seguimiento".
	(Ejemplo: a -> b -> c )
	'''
	if type(padres) is dict and not destino == None:
		stack = []
		vertice = destino
		while vertice:
			stack.append(vertice) 
			vertice = padres[vertice]
	else:
		stack = padres

	while stack:
		print(stack.pop(), end = '')
		if stack:
			print(' -> ', end = '')
			continue
		print()
	return

def imprimirListado(lista, limite = None):
	'''
	Se encarga de Imprimir el resultado de las funciones
	que requieran un formato de "Listado".
	(Ejemplo: a, b, c )
	'''
	if not limite: limite = len(lista)
	for i in range(0, limite):
		print(lista[i], end = '')
		if i+1 < limite: 
			print(', ', end = '')
			continue
		print()
	return

def imprimirPorLotes(lista, tipoLote):
	'''
	Se encarga de Imprimir el resultado de las funciones
	que requieran un formato de a "Lotes".
	(Ejemplo: Lote 1: a, b, c )
	'''
	for i in range(len(lista)):
		print(tipoLote+' ',i+1,': ', sep='', end= '')
		conjunto = lista[i]
		contador = 0
		for j in conjunto:
			print(j, end= '')
			if contador+1 < len(conjunto):
				print(end= ', ')
				contador += 1
		print()
	return

#-------------------------------------------------------------------#
#                         FUNCIONALIDADES                           #
#-------------------------------------------------------------------#
def min_seguimientos(grafo, origen, destino):
	'''
	Imprime el Camino Minimo entre un Vertice de Origen y uno de 
	Destino, si es que fueran conexos.
	'''
	if not origen in grafo.vertices() or destino not in grafo.vertices():
		print("Seguimiento imposible")
		return
	_, padres = caminoMinimo(grafo, origen)
	if destino not in padres.keys():
		print("Seguimiento imposible")
		return
	
	imprimirSeguimiento(padres, destino)

def mas_imp(grafo, cant):
	'''
	Imprime, de mayor a menor Centralidad, los k Vertices con mas 
	Centralidad dentro del grafo.
	'''
	vertices_apariciones = random_walks(grafo, grafo.cantidad_vertices(), grafo.cantidad_vertices())
	verticesOrdPorCentralidad = countingSort(vertices_apariciones, False)

	imprimirListado(verticesOrdPorCentralidad, cant)

def persecucion(grafo, verticesDeOrigen, k):
	'''
	Imprime el Camino Minimo entre un Vertices de Origen 
	y uno de los k Vertices con mayor Centralidad.
	'''
	vertices_apariciones = random_walks(grafo, grafo.cantidad_vertices(), grafo.cantidad_vertices())
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

	imprimirSeguimiento(padresFinal, destinoFinal)

def comunidades(grafo, n):
	'''
	Imprime un listado de comunidades de al menos n integrantes.
	'''
	labels, ady_para_cada_vertice = asignar_labels(grafo)

	dict_comunidades = {}

	iteraciones = 50	#numero al azar para testear con los tiempos este se puede cambiar para bajar los tiempos

	for i in range(0 , iteraciones):

		for v in grafo:
		
			labels[v] = max_freq(v, ady_para_cada_vertice[v], labels)

			if (i == iteraciones - 1):
				integrantes = dict_comunidades.get(labels[v], set())
				integrantes.add(v)
				dict_comunidades[labels[v]] = integrantes

	temp = []
	for conjunto in dict_comunidades.values():
		if len(conjunto) >= n: temp.append(list(conjunto))
	imprimirPorLotes(temp,'Comunidad')

def divulgar(grafo, origen, n):
	'''
	Imprime todos los Vertices a una distancia n o menor,
	al Vertice de Origen.
	'''
	distancias, _ = caminoMinimo(grafo,origen,n)
	lista = []
	for vertice in distancias.keys():
		if vertice == origen: continue
		lista.append(vertice)
	imprimirListado(lista)

def divulgar_ciclo(grafo, origen, n):
	'''
	Imprime un camino de largo n, que empiece y termine 
	en el Vertice pasado por parametro.
	'''
	if not origen in grafo.vertices():
		print("No se encontro recorrido")
		return

	vertices_usados = set()

	vertices_en_ciclo = encontrar_ciclo(grafo, origen, origen, n, vertices_usados)

	if vertices_en_ciclo != None:
		vertices_en_ciclo.append(origen)
		imprimirSeguimiento(vertices_en_ciclo)
	else:
		print("No se encontro recorrido")

def cfc(grafo):
	'''
	Imprime cada conjunto de Vertices entre los cuales,
	todos estan conectados con todos.
	'''
	visitados = set()
	en_cfcs = set()
	orden = {}
	stack1 = []
	stack2 = []
	cfcs = []
	for vertice in grafo:
		if vertice not in visitados:
			orden[vertice] = 0
			_cfc(grafo, vertice, visitados, orden, stack1, stack2, cfcs, en_cfcs)
	imprimirPorLotes(cfcs,'CFC')
