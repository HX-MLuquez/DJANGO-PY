lista_par = []
for i in range(10):
    lista_par.append(2*i + 2)

print(lista_par)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

lista_par_c = [2*n + 2 for n in range(10)]
print(lista_par_c)

valores = [0, 4, 5, 6, 7, 8, 9]  # len(valores)
divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')

valores_c = ['Divisible' if v % 2 == 0 else 'No Divisible' for v in valores]
print(valores_c)
# -> ['Divisible', 'Divisible', 'No Divisible', 'Divisible', 'No Divisible', 'Divisible', 'No Divisible']


lista = ['Lechugas', 'Tomates', 5, 10, True, False, 'Papas', 5.1, 1, 2]
count_str = 0
for elemento in lista:
    if type(elemento) is str:
        count_str += 1
    print(count_str)

lista_resultado = [l for l in lista if type(l) is str] # Filtramos
print(lista_resultado)  # -> ['Lechugas', 'Tomates', 'Papas']

print(f'La cantidad de str en esta lista es {len(lista_resultado)}')
