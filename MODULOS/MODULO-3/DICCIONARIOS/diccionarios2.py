computador = {'notebook': 489990, 'tablet': 120000, 'cargador': 12400}
claves_computador = computador.keys()

print(claves_computador) # dict_keys(['notebook', 'tablet', 'cargador'])

values_computador = computador.values()
print(values_computador) # dict_values([489990, 120000, 12400])

items_computador = computador.items()
print(items_computador) # dict_items([('notebook', 489990), ('tablet', 120000), ('cargador', 12400)])

buscar_dame = computador.get('tablet', 'No se encuentra el elemento solicitado')

print(buscar_dame) # 120000