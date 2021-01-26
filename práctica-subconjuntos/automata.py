import estado

class Automata:

	def __init__(self,alfabeto):
		self.alfabeto = alfabeto # alfabeto que acepta el automata
		self.indice = [] # indice del nodo
		self.transiciones = []
		self.nodos = []

	# metodo que carga un archivo 
	# nombre: nombre del archivo
	def cargar_desde(self,nombre):
		f = open(nombre,'r')
		contenido = f.read()
		# print(contenido)
		i,j = 0,0 # iteradores 
		inicial = "" 
		finales = ""

		# Obtiene el estado incial 
		while ord(contenido[i]) <= 48 or ord(contenido[i]) >= 57: i += 1 #busca el primer numero en la linea
		while contenido[i] != "\n": #Obtine la cadena desde el primer numero hasta el salto de linea
			inicial += contenido[i]
			i += 1
		
		#Obtiene los estados finales
		i += 1 #Para omitir el salto de linea
		while ord(contenido[i]) <= 48 or ord(contenido[i]) >=57: i += 1
		while contenido[i] != "\n":
			finales += contenido[i]
			i += 1
		finales = finales.split(",") #convierte la cadena en un arreglo, separados por ','
		# print(inicial, finales)

		#obtiene las transiciones
		j = i + 1
		# transiciones = []
		while i != len(contenido):
			i += 1
			if i == len(contenido) or contenido[i] == "\n": #Recorre el arreglo lina por linea
				aux = contenido[j:i].split('->') #Crea un arreglo de la cadena separado por '->'
				aux = [aux[0]] + aux[1].split(',') #Crea un arreglo de la segunda mitad de la cadena, separada por ',' y concatena ambos arreglos
				self.transiciones.append(aux)
				j = i + 1
		# print(self.transiciones)
		i = 0
		aux = []
		estados = []
		es_inicial = False
		es_final = False

		for i in range(0,len(self.transiciones)):
			if not(int(self.transiciones[i][0]) in aux):
				aux.append(int(self.transiciones[i][0]))
			elif not(int(self.transiciones[i][1]) in aux):
				aux.append(int(self.transiciones[i][1]))
		aux.sort() # ordeno los estados 

		i = 0
		for i in range(0,len(aux)):
			if str(aux[i]) == inicial:
				es_inicial = True
			if str(aux[i]) in finales:
				es_final = True
			estados.append(estado.Estado(es_inicial,es_final,aux[i]))
			es_inicial = False
			es_final = False

		self.indice = aux
		self.nodos = estados
		self.inicial = inicial
		self.finales = finales
	
		i = 0
		for i in range(0,len(self.transiciones)):
			self.agregar_transicion(int(self.transiciones[i][0]),int(self.transiciones[i][1]),self.transiciones[i][2])


	def agregar_transicion(self,inicio, fin, simbolo):
		# print("---",self.estados.index(inicio),"->",self.estados.index(fin),",",simbolo)
		# print(self.estados.index(fin))
		self.nodos[self.indice.index(inicio)].agregar_transicion(simbolo,self.indice.index(fin))

	def obtener_inicial(self):
		return int(self.inicial)

	def set_indice(self,estados):
		self.indice = estados

	def set_nodos(self,nodos):
		self.nodos = nodos

	def get_alfabeto(self):
		return self.alfabeto

	def get_indice(self):
		return self.indice

	def obtener_finales(self):
		i = 0
		aux = []
		for i in range(0,len(self.finales)):
			aux.append(int(self.finales[i]))
		return aux

	def establecer_inicial(self,estado):
		self.nodos[self.indice.index(estado)].set_inicial(True)

	def establecer_final(self,estado):
		self.nodos[self.indice.index(estado)].set_final(True)

#TODO test
# af = Automata("a,b".split(','))
# af.cargar_desde('af.txt')
