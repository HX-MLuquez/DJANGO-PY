"""
Tenemos un listado de países y la cantidad de usuarios por cada país en la 
siguiente tabla:
1. Convertir la tabla mostrada en un diccionario.
2. Filtrar los países con menos de 60 usuarios.
País Cantidad de usuarios
México 70
Chile 50
Argentina 55
"""
paises = ["México", "Chile", "Argentina"]
usuarios = [70, 50, 55]

diccionario_tabla = {k: v for k,v in zip(paises,usuarios)}
diccionario_tabla2 = dict(zip(paises,usuarios))

print(diccionario_tabla) # {'México': 70, 'Chile': 50, 'Argentina': 55}

resultado_filtrado = {pais: usuario for pais, usuario in diccionario_tabla.items() if usuario >= 60}

print(resultado_filtrado) # -> {'México': 70}
