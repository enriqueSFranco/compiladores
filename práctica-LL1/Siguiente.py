# clase de Siguiente

class Siguiente:
	# constructor de la clase Siguiente
	def __init__(self,primeros,gramatica,noTerminal):
		self.gramatica = gramatica
		self.noTerminal = noTerminal
		self.primeros = primeros
		self.producciones = gramatica.getProducciones() 
		self.conjuntoSiguientes = list(set(self.calcularSiguientes(self.noTerminal)))

	"""
		Metodo para calcular los juntos de siguientes
	"""
	def calcularSiguientes(self, noTerminal):
		if noTerminal == self.gramatica.getSimboloInicial(): 
			temp = ["$"] # guardamos el primero simbolo que se agrega al conjunto de siguientes del simbolo inicial 
		else: # si no es el simbolo inicial 
			temp = []
		for i in self.producciones:
			#Formato de producciones [NoTerminal,lista de producciones([produccion 1, produccion2, etc.])
			for j in i[1]:
				if j.count(noTerminal) >= 1:
					return self.Reglas(noTerminal, i[0], j) + temp
	"""
		Reglas para el calculo de siguientes de un gramatica
		noTerminal
		produccion
	"""
	def Reglas(self,Simbolo,noTerminal,produccion):
		if (produccion.index(Simbolo) + 1) == len(produccion):
			# aB
			if noTerminal != Simbolo and Simbolo != self.gramatica.getSimboloInicial():
				aux = self.calcularSiguientes(noTerminal)
				return aux
			else:
				return []
		else:
			# Sb
			# aSb
			aux = [produccion[len(produccion) - 1]]
			for i in self.primeros:
				if i.getNoTerminal() == produccion[len(produccion) - 1]:
					aux = i.getConjuntosPrimeros()[:]
					if "E" in aux:
						aux.remove("E")
			if noTerminal == Simbolo and Simbolo != self.gramatica.getSimboloInicial():
				return aux 
			elif Simbolo != self.gramatica.getSimboloInicial():
				temp = self.calcularSiguientes(noTerminal)
				return temp + aux
			else:
				return aux

	def getConjuntoSiguientes(self):
		return self.conjuntoSiguientes

	def getNoTerminal(self):
		return self.noTerminal