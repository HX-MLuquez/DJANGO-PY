

lista_par = [] # [0, 1, 2 ... , 9]
for i in range(10):  # (0, 9) -> i [ 0 1 2 3 4 5 6 7 8 9 ] # range(0, 10)
    lista_par.append(i)
    
print(lista_par)
# -> [0,1,2,3,4,5,6,7,8,9]

#* COMPREHENSION
lista_nueva = [i + 100 for i in range(10)] # [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
print(lista_nueva)

lista_nueva = [True for i in range(10)] # [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
print(lista_nueva)
# [True, True, True, True, True, True, True, True, True, True]

#
lista_boolean = [True, False, False, True, True]
# -> [1, 0, 0, 1, 1]
lista_binaria = [1 if b == True else 0 for b in lista_boolean]
print(f'lista binaria -> {lista_binaria}') # -> [1, 0, 0, 1, 1]
