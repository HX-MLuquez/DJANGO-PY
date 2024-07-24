"""
Crear una lista
Agregar 3 elementos (string)
Eliminar el elemento de la pos 1
agregar un cuarto elemento
crear con un for un programa de búsqueda
"""
lista = []

lista.append("hola")
lista.append("boby")
lista.append("la patita")

elimino_pos1 = lista.pop(1)

lista.append("otro mas")

search = input("Ingresa texto a buscar: ").lower()
econtrada = False
for i in lista:
    if i == search:
        econtrada = True
        break
    
if econtrada:
    print("Si se encuentra esa palabra")
else:
    print("NO se encuentra esa palabra")


print("Programa finalizado")
