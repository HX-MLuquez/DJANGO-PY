
# ANIDADOS

for i in [1, 2, 5]:
    for j in [6, 6, 8]:
        print("Hola")

# O n^2   #todo: algunos alg. complejos trabajan así

for i in [1, 2, 5]:
    for j in [6, 9, 8]:
        for k in [2, 1]:
            print("Chau")
# O n^3 #! ERROR

# EJERCICIO GUIADO

# TODO: 2 min de encuesta https://forms.gle/avKKrqnBXbKdRSVs8 y volvemos

# Supongamos que queremos mostrar una tabla de multiplicar, por ejemplo la tabla
# del 5. Esto se puede escribir como:
#  for numero in range(10):
#  print(f"5 * {numero} = {5 * numero}")
#  Ahora bien,
# ¿Cómo podríamos hacer para mostrar todas las tablas de multiplicar del 1 al 10?
# Envolviendo el código anterior en otro ciclo que itere de 1 a 10.

for tabla_de in range(10):
    print(f"La tabla de {tabla_de}")
    for numero in range(11):
        print(f'{tabla_de} * {numero} = {tabla_de * numero}')
        

"""
FOR con un conjunto de elementos claros determinados 

WHILE Iterador que finaliza según una condición

enumerate() -> [3,4,5] -> [(0, 3), (1, 4), (2, 5)] <- ENUMERA, me una posición, anexa un INDEX

zip() -> [3,4,5] + [7,6,9] -> [(3, 7), (4, 6), (5, 9)] <- MEZCLA 2 o más LISTAS

break -> Cuando se ejecuta CORTA el CICLO

"""
