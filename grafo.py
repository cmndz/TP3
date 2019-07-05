class Grafo:
    def __init__(self):
        '''Crea un grafo vacio'''
        self._vertices = {}
        self._cantidadVertices = 0
    def verticeAgregar(self, vertice):
        '''Agrega un vertice'''
        if not vertice in self._vertices.keys():
            self._vertices[vertice] = {}
            self._cantidadVertices += 1
            return True
        return False
    def verticeRemover(self, vertice):
        '''Elimina un vertice'''
        if self.estaVacio() or not vertice in self._vertices.keys():return None
        for w in self._vertices.keys(): 
            if vertice in self._vertices[w].keys(): self._vertices[w].pop(vertice)
        self._cantidadVertices -= 1
        return self._vertices.pop(vertice)
    def verticeCantidad(self):
        '''Devuelve la cantidad de vertices que contiene el grafo'''
        return self._cantidadVertices
    def aristaAgregar(self, verticeOrigen, verticeDestino):
        '''Agrega una arista'''
        if self.estaVacio() or not verticeOrigen in self._vertices.keys() or not verticeDestino in self._vertices.keys():return False
        self._vertices[verticeOrigen][verticeDestino] = ''
        return True
    def aristaRemover(self, verticeOrigen, verticeDestino):
        '''Elimina una arista'''
        if self.estaVacio() or not verticeOrigen in self._vertices.keys() or not verticeDestino in self._vertices.keys():return None
        return self._vertices[verticeOrigen].pop(verticeDestino)
    def estaVacio(self):
        '''Devuelve true si esta vacio, sino false'''
        return self._cantidadVertices == 0
    
    def vertices(self):
        '''Devuelve una lista con los vertices'''
        return self._vertices.keys()
    def adyacentes(self, v):
        '''Devuelve una lista con los adyacentes'''
        return self._vertices[v].keys()
    # def estanConectados(self, a, b):
    #     '''Devuelve true si estan conectados, sino false'''
    #     if not a in self._vertices.keys() or not b in self._vertices.keys():return False
    #     return a in self._vertices[b].keys() and b in self._vertices[a].keys()
    def __str__(self):
        cadena = ""
        for v in self._vertices.keys():
            cadena += v + ":"
            for w in self._vertices[v].keys():
                cadena += w + " "
            cadena += "\n"
        return cadena


