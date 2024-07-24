# Librería / Módulo
import sys

# sys.argv
"""
Indentación
En Python está definida por 
convención en 4 espacios, 
aunque hoy en día prácticamente 
todo editor de texto permite usar un 
Tab, el cual automáticamente se 
transformará en 4 espacios -> tab
"""

# if True:
#     print("hola")
#     print("dede")

# TODO: Maneras de Ingresar datos

"""
nombre = input("Ingrese su nombre: ")
print(f'Mi nombre es {nombre}')

# * USAMOS SYS.ARGV
print(f'Script -> {sys.argv[0]}')

print(f'primer argumento luego del Script original -> {sys.argv[1]}')
print(f'otro argumento luego del Script original -> {sys.argv[2]}')


print(f'El área del rectángulo es {float(sys.argv[1]) * float(sys.argv[2])}')
"""


#                          0       1    2     3
# Script      sys.argv["day6.py", "3", "4", "pepe"]
# Probar con -> python day6.py 3 4 pepe

#                          0
# Script      sys.argv["day6.py"]
# Probar con -> python day6.py
# sys.argv[1]

# TODO: Control de Flujo - Condiciones

# * La instrucción IF
super_hero = input("Eres un super héroe? Si - No\n> ")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: ")) # STRING -> INT

# Operadores de Comparación + Operadores lógicos
# if True:
#     print("Hola")  # Dentro del bloque (según el identado (4 == tab))

# if nombre == "Jimy":  # True
#     print(f"Hola {nombre}")

# if nombre == "John":  # False
#     print(f"Hola {nombre}")

# if edad > 18 and nombre == "Jimy":  # Ambos deben ser True
#     print("si soy Jimy y tengo mas de 18")

# if edad < 30 or nombre == "Jimy": # False - True
#     print("si soy Jimy pero tengo mas de 30")
    

# ANIDAR
# if nombre == "Hulk":
#     print("se cumple una condición HULK")
#     if edad > 30:
#         print("")
#         print("se cumple otra condición edad")
#         if True:
#             print("otroooooo")
#             print("otroooooo queeeeeee????")
         
            
# print("El programa ha finalizado")

# * La instrucción ELSE

# if nombre == "Spiderman":
#     print("Salta el edificio")
#     if edad > 90:
#         print("mejor no saltes")
# else:
#     print("no saltes porque te romperas una pierna")
#     if edad > 20 and edad < 29:
#         print("si quieres inténtalo con un paracaídas")
#     else:
#         print("ni te muevas")



# * La instrucción ELIF
# if edad == 1:
#     print("Tengo un año")
# elif edad == 2:
#     print("Tengo dos año")
# elif edad == 3:
#     print("Tengo tres año")
# elif edad == 4:
#     print("Tengo cuatro año")
# else:
#     print("no tengo ninguna de esas edades")


if super_hero == "Si":
    print("Bienvenido a la liga de la justicia")
    if nombre == "Hulk":
        print("aplasta")
    elif nombre == "Ant-Man":
        print("reduce tu tamaño")
    elif nombre != "Spiderman" and edad > 12:
        print("Que super héroe eres")
    else:
        print("cuando creen que entra???")
else:
    print("nos vemos luego") 
    
#* ANIDAR - MULTIDIMENSIONAL    
# {{{{{{}}}}}}
# [[[[[[[]]]]]]]
# ififififififi

#* Cuando implementar IF ELIF ELSE
price = 102
nivel = 3
# De que el Usuario para cada Nivel es data diferente (6 niveles)
if nivel == 1:
    print("soy nivel 1 y tatatatattaat")
elif nivel == 2:
    print("soy nivel 2 y tatatatattaat")
elif nivel == 3:
    print("soy nivel 3 y tatatatattaat")
elif nivel == 4:
    print("soy nivel 4 y tatatatattaat")
elif nivel == 5:
    print("soy nivel 5 y tatatatattaat")
else:
    print("soy nivel 6 y tatatatattaat")
    
# Divisiones del 1 - 3 del 4 - 5 y el 6
if nivel >= 1 and nivel <= 3:
    print("soy nivel 1 2 3 y tatatatattaat")
elif nivel >= 4 and nivel <= 5 :
    print("soy nivel 4 5 y tatatatattaat")
else:
    print("soy nivel 6 y tatatatattaat")
    
# No va mas el nivel 6
if nivel >= 1 and nivel <= 3:
    print("soy nivel 1 2 3 y tatatatattaat")
else:
    print("soy el resto de los niveles y tatatatattaat")


# A puros IFS
if nivel >= 1 and nivel <= 3:
    print("soy nivel 1 2 3 y tatatatattaat")
if nivel >= 4 and nivel <= 5 :
    print("soy nivel 4 5 y tatatatattaat")
if nivel >= 6:
    print("soy nivel 6 y tatatatattaat")
    
#TODO: Determinar si el número que nuestro usuario ingresa es par o impar

    