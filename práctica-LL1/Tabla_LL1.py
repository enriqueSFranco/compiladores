# clase para la Tabla_LL1 hace uso de los conjuntos de primeros y siguientes 
class Tabla_LL1:
	def __init__(self,gramatica,primeros,siguientes):	
		self.bandera = False
		self.gramatica = gramatica
		self.primeros = primeros
		self.siguientes = siguientes
		self.tabla = self.generarTabla()

	def generarTabla(self):
		columnas = self.gramatica.getTerminal()[:]
		if "E" in columnas:
			columnas[columnas.index("E")] = "$"
		else:
			columnas.append("$")
		ll1 = []
		for i in range(len(self.gramatica.getNoTerminal())):
			ll1.append([])
			if 'E' in self.primeros[i].getConjuntosPrimeros():
				for j in range(len(columnas)):
					if columnas[j] in self.primeros[i].getConjuntosPrimeros():
						ll1[i].append(self.buscar(self.gramatica.getNoTerminal()[i],columnas[j]))
					elif columnas[j] in self.siguientes[i].getConjuntoSiguientes():
						ll1[i].append("E")
					else:
						ll1[i].append(None)
			else:
				for j in range(len(columnas)):
					if columnas[j] in self.primeros[i].getConjuntosPrimeros():
						ll1[i].append(self.buscar(self.gramatica.getNoTerminal()[i],columnas[j]))
					else:
						ll1[i].append(None)
		return ll1

	def buscar(self,no_terminal,simbolo):
		produccion_auxiliar = self.gramatica.getProduccionAsociada(no_terminal)
		self.bandera = False
		correcta = ""
		for i in produccion_auxiliar:
			if i[0] in self.gramatica.getNoTerminal():
				self.buscar(i[0],simbolo)
			else:
				if i[0] == simbolo:
					self.bandera = True
			if self.bandera == True:
				correcta = i
				break
		return correcta

	def getTabla(self):
		return self.tabla
