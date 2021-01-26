class Estado:
	# constructor de la clase 
	def __init__(self,inicial,final, nombre):
		self.inicial = inicial # estado inicial
		self.final = final # estado final 
		self.nombre = nombre # nombre del estado [1]--a-->[2]
		self.transiciones = [] # lista de transiciones 

	#metodo para agregar una transicion 
	def agregar_transicion(self,simbolo,siguiente):
		#print(self.nombre,"->",siguiente+1,",",simbolo)		
		temp = [simbolo,siguiente]
		self.transiciones.append(temp)
	
	def get_transisiones(self):
		return self.transiciones

	# método para borrar las transiciones para un simbolo en especifico
	def eliminar_transicion(self, fin, simbolo):
		del self.transiciones[fin, simbolo]

	# método que devuelve el nombre del nodo
	def getNombre(self):
		return self.nombre

	# método que devuelve si el nodo es final
	def get_final(self):
		return self.final

	# método que asigna si el nodo es final
	def set_final(self, es_final):
		self.final = es_final

	# método que devuelve si el nodo es final
	def get_inicial(self):
		return self.inicial

	# método que asigna si el nodo es final
	def set_inicial(self, es_inicial):
		self.inicial = es_inicial