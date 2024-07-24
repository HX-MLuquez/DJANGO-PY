
# [].append
# [2, 3, 4, 5, 6].append
lista = [2, 3, 4, 5, 6]
# lista.append
# print(lista.__dir__())

lista_copia = lista
lista_copia2 = lista

# * .copy() - CLONE de verdad
copia_clone = lista.copy()

# .append AGREGAR elementos
lista.append("Hola")
lista.append(123)
print(lista)  # [2, 3, 4, 5, 6, 'Hola' 123]

# .insert(i,e) INSERTA desplaza

# insert necesita dos datos (numero_pos, elemento_insert)
lista.insert(2, "Juju")
print(lista)  # [2, 3, "Juju", 4, 5, 6, 'Hola' 123]

# lista.insert(12, "Tomate") #! Siempre toma la última
lista.insert(7, "Tomate")
print(lista)


# .pop()

# [2, 3, 'Juju', 4, 5, 6, 'Hola', 'Tomate', 123]

valor_pop = lista.pop()  # Saca el último elemento de lista

print(lista)  # [2, 3, 'Juju', 4, 5, 6, 'Hola', 'Tomate']
print(valor_pop)

valor_pop_indicado = lista.pop(2)  # Sacar un elemnto según la POS
print(lista)  # [2, 3, 4, 5, 6, 'Hola', 'Tomate']
print(valor_pop_indicado)  # 'Juju'

# * .remove()
lista.append("Hola")
print(lista)
# Remueve según el elemento siendo el primero que encuentra
lista.remove("Hola")
print(lista)  # [2, 3, 4, 5, 6, 'Tomate']

# lista.remove("NO existe") #! ValueError: list.remove(x): x not in list

# * .reverse()
lista.reverse()
print(lista)  # ['Hola', 'Tomate', 6, 5, 4, 3, 2]

# * .sort() - ORDENAMIENTO

lista_numeros = [3, 6, 1, 8, 56]

lista_texto = ["juan", "hola", "miguel"]
lista_numeros.sort(reverse=True)
lista_texto.sort()
print(lista_numeros)
print(lista_texto)


# * sorted()
print(sorted(lista_numeros))
print(sorted(lista_numeros, reverse=True))


print(f'lista_copia ----> ', lista_copia)
print(f'copia_clone ----> ', copia_clone)


# * .index()

print(lista.index("Tomate"))  # 1 <- pos
print("-----------------------------------------------")
# TODO:  Operaciones

# * Concatenaciones - Al concatenar (al SUMAR) nos queda una única lista

# "Hola " + "Mundo" == "Hola Mundo"

lista_mix = lista_texto + lista_numeros

print(lista_mix)

listas_concat = [1] + [2] + [3] + [4]
print(listas_concat)  # [1,2,3,4]

animales = ['Gato', 'Perro', 'Tortuga']
animales_2 = ['Hurón', 'Hamster', 'Erizo de Tierra']

#* Repitiendo listas
animales_actualizados = animales * 4 # ['Gato', 'Perro', 'Tortuga','Gato', 'Perro', 'Tortuga','Gato', 'Perro', 'Tortuga','Gato', 'Perro', 'Tortuga']
mascotas = animales_actualizados + animales_2 # ['Gato', 'Perro', 'Tortuga','Gato', 'Perro', 'Tortuga','Gato', 'Perro', 'Tortuga','Gato', 'Perro', 'Tortuga','Hurón', 'Hamster', 'Erizo de Tierra']
# Veamos algunas características
print(animales_actualizados)
print(len(animales_actualizados))
print(mascotas)
print(len(mascotas))


