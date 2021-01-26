# clase Primero: se encarga de obtener los juntos de primero de una gramatica 
"""
Gramatica 1
A->aAb              P(A) = {a,c}
A->Bbc              P(B) = {c}
B->cb

Gramatica 2
S->E                P(S) = {E, s}
S->sAP              P(P) = {p, q}
P->pASQ             P(Q) = {E, s, q}
Q->SS               P(A) = {a}
Q->qPs
P->q
A->a

"""

class Primero:
    # constructor de Primero
    # gramatica: gramatica con la que se va a trabajar
    # noTerminal: simbolo para Obtener el conjunto de primeros
    def __init__(self,gramatica,noTerminal):
        self.gramatica = gramatica
        self.producciones = gramatica.getProducciones()
        self.noTerminal = noTerminal
        self.ConjuntoPrimeros = [] 
        self.calcularPrimeros(noTerminal)


    """"
        Metodo para calcular el conjunto de primeros de una gramatica
        noTerminal: es el simbolo con cual se calcula el conjunto de primero para dicho simbolo
    """
    def calcularPrimeros(self,noTerminal):
        for i in self.producciones:
            if noTerminal == i[0]: # noTerminal = A ,Produccion = A->aB, ... etc 
                for j in i[1]: # aB
                    if j[0] in self.gramatica.getTerminal() or j[0] == "E": # case: A->aAb 
                        self.ConjuntoPrimeros.append(j[0]) # {a, c}
                    else: # case: A->Bbc
                        self.calcularPrimeros(j[0])

    """
        retorna el conjunto de primeros de una gramatica
    """
    def getConjuntosPrimeros(self):
        return self.ConjuntoPrimeros

    """
        retorna el simbolo no terminal de una gramatica
    """
    def getNoTerminal(self):
        return self.noTerminal

