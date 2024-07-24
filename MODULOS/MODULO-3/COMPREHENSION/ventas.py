#  Dada la información de ventas de 3 meses:
#  1. Convertir la tabla en un diccionario
#  2. Modificar el diccionario para incrementar las ventas en un 10%.
#  3. Hacer un nuevo diccionario pero con las ventas disminuidas un 20%.
#  Mes Ventas
#  Octubre 65000
#  Noviembre 68000
#  Diciembre 72000

mes = ["Octubre", "Noviembre", "Diciembre"]
ventas = [65000, 68000, 72000]

diccionario_tabla = {k: v for k,v in zip(mes,ventas)}
print(diccionario_tabla)

incrementado = {k:v * 1.10 for k,v in diccionario_tabla.items()}
print(incrementado)

decrementado = {k:v * 0.8 for k,v in diccionario_tabla.items()}
print(decrementado)


