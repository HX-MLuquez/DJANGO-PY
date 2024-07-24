
# CONVERTIR

diccionario = {"a":1, "b":2}

lista = diccionario.items() # [("a",1),("b",2)]

print(f'lista --> {lista}')

de_nuevo_diccionario = dict(lista)

print(f'de_nuevo_diccionario --> {de_nuevo_diccionario}')

list()
tuple()
set(lista)

dir(lista)
lista.__dir__()