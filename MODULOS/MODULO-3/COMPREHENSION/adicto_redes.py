lista = [120, 50, 600, 30, 90, 10, 200, 0, 500]
# lista_nueva = ["mal" for min in lista]
# ->  ['mal', 'mal', 'mal', 'mal', 'mal', 'mal', 'mal', 'mal', 'mal']
lista_nueva = ["mal" if min >= 90 else "bien" for min in lista]
print(lista_nueva) # -> ['mal', 'bien', 'mal', 'bien', 'mal', 'bien', 'mal', 'bien', 'mal']
