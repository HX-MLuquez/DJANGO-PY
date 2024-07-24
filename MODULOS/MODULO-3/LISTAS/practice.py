"""
1. Crea una Lista
2. Agrega un elemento
3. Cambia un elemento
4. Elimina un elemento
"""

dulces = ["alfajores", "chocolate en rama", "chicle", "turrón", "caramelos"]

print(dulces)

dulces.append("chupetines")

print(dulces)
# Cambiar es pisar 
dulces[1] = "lo que sea"
print(dulces)

# Eliminar 

salvo_por_las_dudas_antes_del_pop = dulces.pop(3)

print(dulces)
print(salvo_por_las_dudas_antes_del_pop)


