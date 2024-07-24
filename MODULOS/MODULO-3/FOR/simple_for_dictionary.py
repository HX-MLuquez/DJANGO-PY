
#TODO: DICT
# productos = {"producto1": {"id": "231", "tipo": "tv", "marca": "Samsung", "precio": 101},
#              "producto2": {"id": "231", "tipo": "tv", "marca": "Samsung", "precio": 101}
#              }

#            clave  valor, clave  valor,  clave  valor,     clave  valor
producto1 = {"id": "231", "tipo": "tv", "marca": "Samsung", "precio": 101}
print(producto1) # {'id': '231', 'tipo': 'tv', 'marca': 'Samsung', 'precio': 101}

print(producto1['marca']) # -> su value -> 'Samsung'

for clave in producto1:
    print(f'key -> {clave}')
    print(f'value -> {producto1[clave]}')

#* .items()

print(f'>>> {producto1.items()}') # dict_items([('id', '231'), ('tipo', 'tv'), ('marca', 'Samsung'), ('precio', 101)])

for clave, valor in producto1.items():
    print(f'::::::::: {clave} - {valor}')
