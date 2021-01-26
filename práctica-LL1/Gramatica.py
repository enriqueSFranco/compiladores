# clase de Gramatica: define los atributos de una gramatica general G = {NoTerminal, ConjuntoTerminales, Producciones, SimboloInicial}
class Gramatica:
    # constructor de la clase Gramatica
    # linea son las producciones de la gramatica "A->aAb,A->Bbc,B->cb"
    def __init__(self,linea):
        self.simboloInicial = "" # simbolo inicial de la gramatica
        self.noTerminales = [] # conjunto de simbolos no terminlaes de la gramatica 
        self.buscarNoTerminal(linea)
        self.producciones = self.buscarProducciones(linea) 
        self.terminales = [] # conjunto de simbolos terminales
        for i in self.producciones:
            self.buscarTerminal(i[1])
    """
        Metodo que busca un simbolo no terminal en una gramatica
        produccion: es la produccion de una gramatica para buscar su simbolo terminal A->bA, simbolo terminal b
    """
    def buscarTerminal(self, produccion):
        for i in produccion:
            for j in range(len(i)):
                if not i[j] in self.noTerminales:
                    if not i[j] in self.terminales:
                        self.terminales.append(i[j])                       
    
    """
        Metodo que busca un simbolo no terminal en una gramatica
        produccion: es la produccion de una gramatica para buscar su simbolo terminal A->bA, simbolo terminal A
    """
    def buscarNoTerminal(self,linea):
        entrada = linea.split(",") # 
        for i in range(len(entrada)):
            indice = entrada[i].index("-") # ""->
            cadenaSimbolos = entrada[i][:indice].strip()
            # print("cadenaSimbolos:",cadenaSimbolos)
            if not cadenaSimbolos in self.noTerminales:
                self.noTerminales.append(cadenaSimbolos)
        self.simboloInicial = self.noTerminales[0]
   

    def buscarProducciones(self,linea):
        aux = linea.split(",") #creamos una lista auxiliar con las produccion
        producciones = [] # lista para almacenar las producciones
        for i in self.noTerminales:
            producciones.append([i,[]]) # [['A', ['aAb', 'Bbc']], ['B', ['cb']]]
        for i in range(len(aux)):
            # print("--",aux[i][(aux[i].index(">") + 1):])
            produccionAux = aux[i][(aux[i].index(">") + 1):].strip().split(",")
            # print("produccionAux",produccionAux)
            indice = self.noTerminales.index(aux[i][:aux[i].index("-")].strip())
            producciones[indice][1] = producciones[indice][1] + produccionAux
        return producciones

    """
        Metodo que busca una produccion de acuerdo un simbolo no terminal
        noTerminal: simbolo no terminal de una produccion de la gramatica
    """
    def getProduccionAsociada(self,noTerminal):
        return self.producciones[self.noTerminales.index(noTerminal)][1]

    # get() y set() 
    def getTerminal(self):
        return self.terminales

    def setTerminal(self, terminales):
        self.terminales = terminales
    
    def getNoTerminal(self):
        return self.noTerminales
    
    def setNoTerminal(self, noTerminales):
        self.noTerminales = noTerminales
    
    def getProducciones(self):
        return self.producciones
    
    def setProducciones(self, producciones):
        self.producciones = producciones
    
    def getSimboloInicial(self):
        return self.simboloInicial
    
    def setSimboloInicial(self, simboloInicial):
        self.simboloInicial = simboloInicial

# producciones = "A->aAb,A->Bbc,B->cb"
# g = Gramatica(producciones)

# print(g.getNoTerminal())
# print(g.buscarProducciones(producciones))
# print(g.getTerminal())
# print(g.getSimboloInicial())
# print(g.getProducciones())

