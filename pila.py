class Pila:
	"""Representación del TAD Pila."""

	def __init__(self):
		"""Constructor del TAD Pila."""
		self.datos = []
		self.cantidad = 0


	def esta_vacia(self):
		"""Devuelve verdadero si la pila no tiene elementos apilados, false en caso contrario."""
		return not self.cantidad


	def apilar(self, dato):
		"""Agrega un nuevo elemento a la pila."""
		self.datos.insert(self.cantidad, dato)
		self.cantidad += 1


	def ver_tope(self):
		"""Obtiene el valor del tope de la pila. Si la pila tiene elementos,
		se devuelve el valor del tope. Si está vacía devuelve None."""
		if self.esta_vacia():
			return None

		return self.datos[self.cantidad - 1]


	def desapilar(self):
		"""Saca el elemento tope de la pila. Si la pila tiene elementos, se quita el
		tope de la pila, y se devuelve ese valor. Si la pila está vacía, devuelve
		None."""
		if self.esta_vacia():
			return None

		self.cantidad -= 1
		return self.datos[self.cantidad]