class Estado:
    # constructor de la clase Estado
    def __init__(self, inicial, final):
      self.__final = final 
      self.__inicial = inicial 
      self.__transiciones = [] 

    # metodo que agrega una transicion al nodo
    def agregar_transicion(self, final, simbolo):
        # print(self.__id,"->",final+1,",",simbolo)
        temp = [final, simbolo]
        self.__transiciones.append(temp)
    
    # metodo que devuelve las transiciones a partir de un simbolo
    def obtener_transiciones(self):
        return self.__transiciones
    
    # metodo para borrar la transicion de un simbolo en especifico
    def eliminar_transicion(self, fin, simbolo):
        del self.__transiciones[fin, simbolo] # eliminamos la referencia 
   
    def establecer_inicial(self, inicial):
        self.__inicial = inicial
    
    def obtener_inicial(self):
        return self.__inicial
        
    # metodo que devuelve el estado final
    def obtener_final(self):
        return self.__final

    # metodo que asigna si el estado es final 
    def establecer_final(self, final):
        self.__final = final


# TODO test
# simbolo = 'a'
# e = Estado(0, 1)
# e.establecer_inicial(0)
# e.establecer_final(1)
# e.agregar_transicion(e.obtener_final(), 'a')
# e.eliminar_transicion(e.obtener_final(), 'a')
# print(e.obtener_transiciones())
# print(e.obtener_final())

