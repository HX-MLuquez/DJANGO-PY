

with open("texto.txt", "r") as file:
    texto = file.read()

print("texto -> ", list(texto.split(" ")))
lista = list(texto.split(" "))


# texto ->  ['Muchacha', 'ojos', 'de', 'papel,', 'adonde', 'vas,', 'quedate', 'hasta', 'el', 
# 'alba;', 'muchacha', 'pequeÃ±os', 'piÃ©s,', 'adonde', 'vas', '...']
lista_set = set(texto)
print("lista_set -> ", list(texto.split(" ")))
# Contar veces aparece la palabra muchacha
contador = 0

for p in lista:
    if p.lower() == "muchacha":
        contador += 1

print(f'muchacha aparece {contador} veces')


sin_repeticiones = set(lista)
print(sin_repeticiones)
# len(set(lista))

print("-------------------------------------------------")
# Saber las posiciones donde aparece la palabra muchacha. Tenemos un texto -> Lista  Salida -> Lista

# -> [1,5,8]

#TODO: IMPORTANTE
#* DEFINIR LOS DATOS de IN y de OUTPUT
i = 0
resultado_pos = []
for l in lista:
    if l.lower() == "muchacha":
        resultado_pos.append(i)
    i += 1
    
print(f'la palabra muchacha aparece en las pos. {resultado_pos}')

#* INDEX
# [[][][][][][]]

# [[[[[[[]]]]]]]