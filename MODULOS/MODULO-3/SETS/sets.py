
#TODO: SET lo pensamos como una lista pero sin elementos duplicados DIFERENTE -> son colecciones NO ORDENADAS 
#* NO INDEX
muchos_animales = {'Gato', 'Perro', 'Tortuga',
                   'Gato', 'Perro', 'Tortuga',
                   'Gato', 'Perro', 'Tortuga',
                   'Gato', 'Perro', 'Tortuga',
                   'Hurón', 'Hamster', 'Erizo de Tierra'}
# no hay duplicados, sólo valores únicos
print(muchos_animales) # {'Hamster', 'Erizo de Tierra', 'Tortuga', 'Gato', 'Hurón', 'Perro'}

muchos_animales.add("Conejo")
print(muchos_animales)

muchos_animales.remove("Erizo de Tierra")
print(muchos_animales)

muchos_animales.add("Otra cosa")
print(muchos_animales)
otros_mas = { "Loro", "León"}

todos = muchos_animales.union(otros_mas)
print(todos)

#TODO: FOR para LIST TUPLE SET es igual

for element in todos:
    print(element)
    
    
"""
Hacer 2 sets
Unirlos   .union()
Agregar un elemento  .add()
Remover un elemento  .remove()
"""
un_set = {"mesa", "silla"}
otro_set = {"ventana", "cuerda", "clavo"}
union_set = un_set.union(otro_set)
print(union_set) # {'mesa', 'cuerda', 'silla', 'ventana', 'clavo'}

union_set.remove("cuerda")
union_set.add("tornillo")
union_set.add("silla")
print(union_set) # {'tornillo', 'mesa', 'silla', 'ventana', 'clavo'}
