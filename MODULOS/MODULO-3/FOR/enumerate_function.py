
#* AYUDA a tener un index. una pos

texto = "hi children ..."

print(enumerate(texto)) # <enumerate object at 0x000001E127955E90>
print(list(enumerate(texto))) # [(0, 'h'), (1, 'i'), (2, ' '), (3, 'c'), (4, 'h'), (5, 'i'), (6, 'l'), (7, 'd'), (8, 'r'), (9, 'e'), (10, 'n'), (11, ' '), (12, '.'), (13, '.'), (14, '.')]

# Devuelve algo similar a lo que devuelve ITEMS, una Lista donde cada elemento está partido en dos elementos

for pos, caracter in enumerate(texto):
    print(f' pos -> {pos} - {caracter}') 
    
