from grafo import * 

def caminoMinimo(grafo, origen):
    visitados = {}
    distancia = {}
    padre = {}
    q = []
    #-----
    for v in grafo.vertices():distancia[v] = None
    #-----
    visitados[origen] = True
    distancia[origen] = 0
    padre[origen] = None
    q.append(origen)
    #-----
    while q:
        v = q.pop(0)
        for w in grafo.adyacentes(v):
            if not w in visitados.keys():
                visitados[w] = True
                distancia[w] = distancia[v]+1
                padre[w] = v
                q.append(w)
    return distancia, padre

def min_seguimientos(grafo, origen, destino):
    '''Imprime el Camino Minimo entre un Vertice de Origen y uno de Destino, si es que fueran conexos.'''
    if not origen in grafo.vertices() or destino not in grafo.vertices():
        print("Seguimiento Imposible")
        return
    
    distancia, padre = caminoMinimo(grafo, origen)
    if not distancia[destino]:
        print("Seguimiento Imposible")
        return

    lista = []
    lista.append(destino)
    v = padre[destino]
    while v:
        lista.append(v)
        v = padre[v]
    lista.reverse()
    print(lista[0], end = "")
    for v in lista[1:]:print(" -> ", v , sep = "", end = "")
    print()
    return

def mas_imp(grafo, cant):
    '''Imprime los Vertices de mayor a menor centralidad dentro del grafo'''
    






g = Grafo()
print(g)
print("Esta vacio?", g.estaVacio())
print("Agrego A",g.verticeAgregar('A'))
print("Agrego B",g.verticeAgregar('B'))
print("Agrego C",g.verticeAgregar('C'))
print("Agrego D",g.verticeAgregar('D'))
print("Agrego E",g.verticeAgregar('E'))
print("Agrego F",g.verticeAgregar('F'))
print("Esta vacio?", g.estaVacio())
print("Cantidad?", g.verticeCantidad())
print("Agrego AB",g.aristaAgregar('A','B'))
print("Agrego BC",g.aristaAgregar('B','C'))
print("Agrego CD",g.aristaAgregar('C','D'))
print("Agrego AE",g.aristaAgregar('A','E'))
print("Agrego BF",g.aristaAgregar('B','F'))
print("Agrego DF",g.aristaAgregar('D','F'))
print("Agrego DF",g.aristaAgregar('D','F'))
print("Agrego DF",g.aristaAgregar('D','F'))
print(g)
#print('Adyacentes de A',g.adyacentes('A'))
min_seguimientos(g, 'A', 'F')
print("Remuevo DF",g.aristaRemover('B','F'))
print(g)
min_seguimientos(g, 'A', 'F')
print("Remuevo B", g.verticeRemover('B'))

#g.verticeRemover('A')
#g.verticeRemover('B')
#print(g.vertices())
#print(g.)