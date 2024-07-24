# FOR
# Requiere un conjunto de Elementos list tuple dict set 

autos = ["bmw", "mercedes", "ford"] # list

i = 1 # Convención / Buenas prácticas
print(len(autos))
for auto in autos:
    print(auto)
    print("hola")
    if auto == "mercedes":
        break
    
texto = "he aquí la primera vez que ..."

for t in texto:
    print(f'-> {t}')
    
    
texto2 = "hola mundo"
i = 1
for letra in texto2:
    if letra != " ":
        print(f'>>> {i} {letra}')
        i += 1
        

frutas = ["pera", "ananá", "banana"]
for fruta in frutas: # Iterará 3 veces
    print(f'fruta -> {fruta}')

productos = ["tv", "pc", "usb", "memoria"]
for producto in productos: # Iterará 4 veces
    print(f'producto -> {producto}')

perros = ["chao chao", "pequiné", "galgo", "pichichu", "kiltro", "terry", "boby"]
for perro in perros: # Iterará 7 veces
    print(f'perro -> {perro}')
    
poesia = "El cielo está ."
j = 1

for p in poesia: # Iterará 15 veces
    print(f'p -> {j} -> {p}')
    j += 1