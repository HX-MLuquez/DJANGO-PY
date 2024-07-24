# FOR LIST
lista = [23, 43, 12, "Hola", False, "Mundo", "Hoy", 44, True, 10]

lista_nueva = [] # append

for elemento in lista:
    if type(elemento) is str:
        lista_nueva.append(elemento)
        
lista = lista_nueva
print(f'La lista filtrada solo con str es {lista}')

# FOR TEXTO
texto = "Había una vez ..."

letra = "e"
contador = 0

for t in texto:
    if t.lower() == letra.lower():
        contador += 1

if contador != 0:
    print(f'La letra "{letra}" aparece en el texto {contador} vez/ces')
else:
    print("Esa letra no se encuentra en este texto")

# FOR DICT
lista1 = ["marca", "tipo", "categoria"]
lista2 = ["adidas", "calzado", "deportiva"]

crear_diccionario = zip(lista1, lista2)

diccionario = {"marca": "adidas", "tipo": "calzado", "categoria": "deportiva"}
# .items -> [("marca": "adidas"), ("tipo": "calzado"), ("categoria": "deportiva")]

deportiva = False
for clave, valor in diccionario.items():
    if clave == "categoria" and valor == "deportiva":
        deportiva = True

if deportiva:
    print("La ropa si es deportiva")
else:
    print("La ropa no es deportiva")

