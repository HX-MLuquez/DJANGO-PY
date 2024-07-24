
import sys 
precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}
umbral = float(sys.argv[1])
#                {}     number
def filtra(diccionario, umbral, mayor_menor = True):
    print()
    if mayor_menor:
        filtrado = {"precio>umbral"}
    else:
        filtrado = {"precio<umbral"}

if len(sys.argv) == 2:
    filtra(precios, umbral)
else:
    if sys.argv[2] == "mayor":
        print("")
    elif sys.argv[2] == "menor":
        print("")
    else:
        print("")

