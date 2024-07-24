# VALOR vs REFERENCIA (puntero)

# Tipos de Datos Primitivos STR BOOL NUMBER 
# Objetos <-> CLASS <- Tipos de datos especiales  LIST []   DICT {}  SET {}  TUPLE ()

contador = 55

copia_numero = contador
copia_numero = "Hola mundo"

lista = [7,8,5]
copia_real_clone1 = lista.copy() # .copy()
copia_real_clone2 = [l for l in lista] # Comprehension

copia_lista = lista
print(id(copia_lista))
print(id(lista))

copia_lista.pop() 
print(lista) # [7,8]

print(copia_real_clone1) # [7,8,5]


diccionario_original = {"a":1, "b":2}
copia_real_dict1 = diccionario_original.copy()
copia_real_dict2 = {k:v for k,v in diccionario_original.items()}

print(id(diccionario_original))
print(id(copia_real_dict1))