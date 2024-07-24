
# Operadores de Comparación
# ==
# !=
# <
# >
# <=
# >=

# Operadores Lógicos
# and
# or
# xor ^

# if
# elif
# else

#* while not "condition"
# Es un bucle (un iterador) != FOR trabajamos sobre una cantidad conocida de elementos
# Se repite mientras la condición se cumpla


# swap = True 

# while swap:
#     user = input("Ingrese usuario ")
#     if user == "Pepe":
#         swap = False 
        
# print("Fin del CODE")

# Factorial de un número
# 3 -> 3 * 2 * 1 = 6
# 2 -> 2 * 1 = 2
# 1 -> 1
# 0 -> 1 
#! No usaremos negativos

numero = int(input("Ingrese el número > "))

print(numero) # 3    ----> 3 * 2 * 1 = 6

if numero < 0:
    print("No vamos a trabajar con negativos")
elif numero == 0:
    print(f"El factorial de {numero} es 1")
else:
    result = 1   # 1
    n = numero   # 3
    while n > 1: 
        result = result * n  #  -> 3  * 2 -> 6
        n -= 1 # -> 2 -> 1
        
    print(f'El factorial de {numero} es {result}')

user= "JIMBO"
edad= 32
#            True           True
#                  True               or    False   --> True
while (user == "JIMBO" and edad == 32) or 1 == 14:
    print("Dentroooo del WHILE")
    edad -= 1 # Caso Base | Corte
print("Fuera del while") 


lista = ["hola", "hi", "Chis"] #  ["hola"]

print(len(lista)) # -> 3

#           1   >  1 -> False
while len(lista) > 1:
    lista.pop()   # -> ["hola", "hi", "Chis"].pop ["hola", "hi"].pop ["hola"].pop []
    
print(f'---> {lista}') # ---> ["hola"]