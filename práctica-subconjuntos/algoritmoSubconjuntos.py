import automata

# funcion cerradura epsilon
def cerradura_E(AF, estado, conjunto):
	if len(AF.nodos[estado].get_transisiones()) == 0: 
		if not(estado in conjunto):
			conjunto.append(estado)
	else:
		i = 0
		for i in range(0,len(AF.nodos[estado].get_transisiones())):
			if not(estado in conjunto):
				conjunto.append(estado)
			if AF.nodos[estado].get_transisiones()[i][0] == 'E': # si el estado que se esta analizando tiene transicion con E se agrega al conjunto
				cerradura_E(AF,AF.nodos[estado].get_transisiones()[i][1],conjunto)

# funcion mover
def mover(AF,conjunto,simbolo):
	conjunto_resultado = [] # lista que contendra el conjunto de estados con el que se pueda hacer la transicion con un simbolo del alfabeto
	i = 0 # iterador para los estados de cerradura-E
	j = 0 # iterador para las transiciones de cada estado del conjunto cerradura-E
	for i in range(0,len(conjunto)): # iteramos sobre los estados del conjunto
		# print(conjunto[i]) -> [0, 1, 2, 4, 7]
		for j in range(0,len(AF.nodos[conjunto[i]].get_transisiones())): # iteramos sobre las transiciones de cada destado del conjunto generado por cerradura-E
			if AF.nodos[conjunto[i]].get_transisiones()[j][0] == simbolo: # analizamos la transicion del estado actual con el simbolo 
				if not(AF.nodos[conjunto[i]].get_transisiones()[j][1] in conjunto_resultado): # verificamos que el estado no exista para agregarlo al conjunto resultado y no tener estados repetidos
					conjunto_resultado.append(AF.nodos[conjunto[i]].get_transisiones()[j][1]) # si tiene transiciones con el simbolo se agrega a la lista de conjunto resultado
	return conjunto_resultado

# funcion Dtran
def Dtran(AF,conjunto,simbolo):
	conjunto_resultado = mover(AF,conjunto,simbolo)
	conjunto = []
	for i in range(0,len(conjunto_resultado)):
		cerradura_E(autom,conjunto_resultado[i],conjunto)
	return sorted(conjunto)

# creamos un objeto de la clase Automata
autom = automata.Automata("a,b".split(','))
autom.cargar_desde('af.txt')

tabla_transicion = [] # almacenamos los estados marcados para el AFN
conjunto = [] # conjunto de estados que se etiquetaran

cerradura_E(autom,autom.get_estados().index(autom.obtener_inicial()),conjunto) # aplicamos cerradura_E al estado inicial del AFN original
tabla_transicion.append(conjunto) # agregamos el primero conjunto por defecto que esl de aplicar cerradura_E [0, 1, 2, 4, 7]
transiciones_AFD = []

i = 0
while i < len(tabla_transicion): # 1
	j = 0
	for j in range(0,len(autom.get_alfabeto())):
		aux = Dtran(autom,tabla_transicion[i],autom.get_alfabeto()[j]) # obtenemos nuevos estados con todos los simbolos del alfabeto
		if not(aux in tabla_transicion): 
			tabla_transicion.append(aux) # [[0, 1, 2, 4, 7], [1, 2, 3, 4, 6, 7, 8]]
		transiciones_AFD.append([i + 1,tabla_transicion.index(aux) + 1,autom.get_alfabeto()[j]])
	i += 1

i = 0
for i in range(0,len(transiciones_AFD)):
	print(transiciones_AFD[i])