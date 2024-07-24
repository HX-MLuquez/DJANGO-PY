
# * K : V    { }
diccionario = {
    "variable1": 1,
    "variable2": 2,
}
#        0 1 2 3
lista = [2, 4, 3, 7]

lista[2]

diccionario["variable1"]

diccionario2 = {"a": 25, "b": 31, "c": "hola"}
print(diccionario2["c"])  # -> "hola"

notas = {
    "Camila": 7,
    "Antonio": 5,
    "Felipe": 6,
    "Daniela": 5,
    "Vicente": 7,
}
# print(notas["felipe"]) #! KeyError: 'felipe'

# * La KEY debe ser única

notas["nueva_data"] = "Holitis"
print(notas)

notas["Daniela"] = "noooooooooooo, la pisé mal"
print(notas)

nombre = "HULK"

nombre = False

# * Agregué un elemento nuevo
notas["camello"] = "soy uno nuevo---------"
print(notas)

# * Cambié el valor de un elemento
notas["camello"] = 101
print(notas)

# * ELIMINAR - DEL POP

diccionario = {"celular": 140000, "notebook": 489990,
               "tablet": 120000, "cargador": 12400}
del diccionario["celular"]
print(diccionario)

salvo_la_data_que_elimine = diccionario.pop("cargador") #! RECOMENDADO
print(diccionario)
print(salvo_la_data_que_elimine)


diccionario.pop("notebook") 


print(f'se eliminó muy bien este dato {salvo_la_data_que_elimine}')

#* UNIR - CONCATENAR      .update()

dicc1 = {"a":1,"b":2}
dicc2 = {"c":3,"d":4}
dicc1.update(dicc2)

print(dicc1) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#! DANGER COLISIONES (datos que se pisan) <- KEY es única
dicc1 = {"a":1,"b":2}
dicc2 = {"a":3,"b":4}
dicc1.update(dicc2)

print(dicc1) # -> {'a': 3, 'b': 4}