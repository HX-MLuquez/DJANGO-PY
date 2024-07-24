"""
1. Crea un diccionario
2. Agrega un elemento
3. Cambia un elemento
4. Elimina un elemento
"""

instrumentos = {}
instrumentos["guitarra"] = "acústica"
instrumentos["ukelele"] = "4 D"
instrumentos["teclado"] = "eléctrico"
instrumentos["oboe"] = "rígido"
print(instrumentos)

instrumentos["oboe"] = "madera arce"
print(instrumentos)

salvo_antes_de_eliminar = instrumentos.pop("ukelele")
print(instrumentos)
print(salvo_antes_de_eliminar)


# [{}{}{}{}]
