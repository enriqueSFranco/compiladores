import Gramatica as Gr
import Primero as Pr
import Siguiente as Sig
import Tabla_LL1 as TLL


def Mostrar(matriz,noTerminales):
	i = 0
	for fila in matriz:
		print(noTerminales[i], end=" ")
		i = i + 1
		for valor in fila:
			print("\t", valor, end=" ")
		print()


# Ejemplos de gramaticas 
producciones = "A->aAb,A->Bbc,B->cb"
#producciones = "S->E,S->sAP,P->pASQ,Q->SS,Q->qPs,P->q,A->a"
#producciones = " S->QP,P->+QP|-QP|E,Q->TA,A->*TA|/TA|E,T->(S)|a|b"

gramatica = Gr.Gramatica(producciones)
noTerminales = gramatica.getNoTerminal()
print("No terminales: ")
print(noTerminales)
primeros = []
siguientes = []
print("Producciones: ")
for i in gramatica.getProducciones():
		print(i)

print("Conjunto primeros: ")
for i in range(len(noTerminales)):
    primeros.append(Pr.Primero(gramatica,noTerminales[i]))
    print(noTerminales[i] + " = {" + str(primeros[i].getConjuntosPrimeros()) + "}")

print("Conjunto siguientes: ")
for i in range(len(noTerminales)):
	siguientes.append(Sig.Siguiente(primeros,gramatica,noTerminales[i]))
	print(noTerminales[i] + " = {" + str(siguientes[i].getConjuntoSiguientes()) + "}")

tabla = TLL.Tabla_LL1(gramatica,primeros,siguientes)


aux_tabla = tabla.getTabla()
columnas = gramatica.getTerminal()[:]
if "E" in columnas:
	columnas[columnas.index("E")] = "$"
else:
	columnas.append("$")

print("\nTabla LL1\n\n")
for valor in columnas:
    print("\t", valor, end=" ")
print("\n")
Mostrar(aux_tabla,noTerminales)





"""
S->E,S->sAP,P->pASQ,Q->SS,Q->qPs,P->q,A->a

S->E 
S->sAP
P->pASQ
Q->SS
Q->qPs
P->q
A->a

Primeros
S = {E,s}
P = {p,q}
Q = {q,s,E}
A = {a}

Siguientes
S = {$,q,s}
P = {$,q,s}
Q = {$,q,s}
A = {p,q,$,s}

S->QP,P->+QP|-QP|E,Q->TA,A->*TA|/TA|E,T->(S)|a|b

S->QP
P->+QP|-QP|E
Q->TA
A->*TA|/TA|E
T->(S)|a|b


Primeros
S = {(,a,b}
P = {+,-,E}
Q = {(,a,b}
A = {*,/,E}
T = {(,a,b}

Siguientes
S = {$,)}
P = {$,)}
Q = {+,-,$,)}
A = {+,-,$,)}
T = {+,/,*,-,$}

"""