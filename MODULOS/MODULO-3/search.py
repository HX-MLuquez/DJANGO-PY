import sys
import random
lista = [1,2,3,4,5,6,7,8,9,0]
 # .shuffle de la librería random permite mezclar
 # la lista de dígitos para aumentar un poco la dificultad.
random.shuffle(lista) # [4, 2, 1, 7, 8, 5, 6, 9, 3, 0]

buscar = int(sys.argv[1]) 
print(lista)
print(buscar)

for pos, elemento in enumerate(lista):
    if elemento == buscar:
        print("Elemento encontrado")
        break 
    # else:
    #     print("Elemento No encontrado")

print("Fin del ciclo")
print(f'El elemento {buscar} se encuentra en la pos {pos}')

"""
input ->
python search.py 3

output -> 
[0, 5, 7, 3, 6, 4, 9, 8, 1, 2]
3
Elemento No encontrado
Elemento No encontrado
Elemento No encontrado
Elemento encontrado
Fin del ciclo
El elemento 3 se encuentra en la pos 3
"""

pos = 0
for n in lista:
    pos += 1
    if elemento == buscar:
        print("Elemento encontrado")
        break
print(f' >> {buscar} - {pos}')