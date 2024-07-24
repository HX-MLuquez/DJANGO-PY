claves = ['nombre', 'apellido', 'edad', 'altura']
valores = ['Juan', 'Pérez', 33, 1.75]

print({k: v for k, v in zip(claves, valores)})
# -> {'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 33, 'altura': 1.75}


tuplas = [("a", 1), ("b", 2), ("c", 3)]

diccionario_nuevo = {k: v for k,v in tuplas}
print(diccionario_nuevo) # -> {'a': 1, 'b': 2, 'c': 3}


# ----------------------------------------

personas = {"Jony": 21, "Boby": 101, "Jimy": 76}

# Filtrar por los > de 30

personas_filtradas = {nombre: edad for nombre, edad in personas.items() if edad > 30}
print(personas_filtradas) # -> {'Boby': 101, 'Jimy': 76}
