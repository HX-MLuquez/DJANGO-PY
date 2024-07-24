
# Practicando DICCIONARIO
usuario1 = {
    "nombre": "Jimy",
    "email": "ma@gmail.com",
    "edad": 34,
    "trabajo": "dev",
    "estado civil": "solo"
}

# hacer una copia clone real  - .copy()
# Trabajar sobre el clone:
# agregar una prop     -  dicc["nueva"] = "nuevo value"
# editar otra prop     -   dicc["key existente"] = "nuevo value"
# eliminar una prop (elemento)    -  dicc.pop("nueva")
# recorrer e imprimir los values   -   for    .items()

# crear una lista de sus keys     .keys()

# obtener (buscar) una prop en particular     .get("prop", "mensaje manejo error")
copia = usuario1.copy()
print(f'original -> {usuario1}')
print(f'copia -> {copia}')
copia["altura"] = 1.78
print(f'original -> {usuario1}')
print(f'copia -> {copia}')

copia["estado civil"] = "acompañado"
print(f'copia -> {copia}')

copia.pop("edad")
print(f'copia -> {copia}')

for k, v in copia.items():
    print(v)

lista_claves = copia.keys()
# dict_keys(['nombre', 'email', 'trabajo', 'estado civil', 'altura'])
print(lista_claves)

resultado_get_copia = copia.get("altura", "No posee altura")
resultado_get_original = usuario1.get("altura", "No posee altura")

print(resultado_get_copia) # 1.78
print(resultado_get_original)  # No posee altura

