
#* LISTAS  VARIEDAD datos - MUTABLE - ÍNDICE (ordenada)

frutas = ["piña", "limón", "tomate", "naranja"]

lista_de_datos_variados = [101, [], {}, "code", "info", True]

print(lista_de_datos_variados)


lista_copia_referencia = lista_de_datos_variados # COPIA por REFERENCIA 

lista_copia_referencia[1] = "gato"

print("original", lista_de_datos_variados)
print("copia   ", lista_copia_referencia)


num1 = 34 
numCopia = num1

print("numCopia", numCopia)

numCopia = numCopia + 1

print("numCopia", numCopia)
print("num1", num1)

print("---------------------------------------")

#            0        1         2
muebles = ["mesa", "silla", "repisa"]

print(len(muebles)) # n -> 3
print(muebles[len(muebles) - 1])

i = 0 # LISTA i -> += 1   IZQ  a DERECHA

i = len(muebles) - 1 # LISTA i -> -= 1   DERECHA a IZQ 
 
print(muebles[1])

# print(muebles[20]) #! IndexError: list index out of range
# print(muebles[len(muebles)]) #! IndexError: list index out of range

#* Mejor manera de acceder a último elemento
print("--------- [-1] -------")
print(muebles[- 1])
print(muebles[- 2])