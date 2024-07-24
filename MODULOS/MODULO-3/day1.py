

# pepe="hola"

# pepe=3

# #todo: IMPERATIVO
# # [2,4,1,3]
# # Obtener suma total
# # paso 1. recorrer esa lista
# # paso 2. ir acumulando en una variable valor + valor
# # paso 3. imprimir resultado

# #todo: DECLARATIVO
# # .algo(lista) -> resultado

# dede = 7

# print("hola")


#! IMPORTANTE - ENTORNO VIRTUAL


#####################################################


# * PRINT()

print("Hola mundo!!!")

#* COMILLAS SIMPLES y/o COMILLAS DOBLES

print('Hola mundo con comillas simples!!!')

print("Hola voy a resaltar con 'comillas' simples un texto determinado en comillas dobles mundo!!!")


# todo: COMENTARIOS

# * EN UNA LÍNEA

# Es este mismo -> # <-


# * EN VARIAS LÍNEAS
"""
Aquí puedo escribir todo todo en
varias líneas
si si si
"""

# todo: PRINT()
# print("Esto es una suma")
print("Esto es otra suma =>", 5+4)
print(f"Resultado de la suma -> {2+5}")

nombre = "Mauricio Gastón"
apellido = "Lúquez"

# todo: FORMAT
print(f"Mi nombre es: {nombre} {apellido}")

# todo: OPERADORES
resta = 23-3

print(f"El resultado de la resta es: {resta}")

mult = 5*3

print(f"El resultado de la multiplicación es: {mult}")

div = 21/3

print(f"El resultado de la división es: {div}")

# result = "dede" + 3 #! TypeError: can only concatenate str (not "int") to str
# print(f"Viendo ERROR -> {result}")


# todo: EMPEZAMOS A INTERPRETAR BIEN LAS LECTURAS de los ERRORES

#! IMPORTANTE, dentro de las triples comillas no usar esta barra -> \ y reemplazar por estas -> /
"""
Traceback (most recent call last):                                             |
  File "C:/Users/mauuu/OneDrive/Escritorio/OTEC 2024/MODULO-3/ejemplo1.py", line 73, in <module>
    result = "dede" + 3
             ~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
"""

# todo: CONCATENANDO STRING (cadena de caracteres)
mensaje1 = "Buenas"
mensaje2 = "soy el segundo mensaje"
concatenoMensajes = mensaje1 + " " + mensaje2
print(f"viendo como concatener string --> {concatenoMensajes}")


"""
COMENTAR en VSC     CTRL + K + C
DESCOMENTAR en VSC  CTRL + K + U

IDENTAR  shift + alt + F

SAVE  CTRL + S

IR HACIA ATRAS   CTRL + Z
IR HACIA DELANTE   CTRL + Y
"""

#* EJERCICIO - CALCULANDO
#   (((z  +   w)   *   x) - a) / b
z = 101
w = 73
x = 3
a = 5 
b = 6  

resultado1 = z + w
resultado2 = resultado1 * x 
resultado3 = resultado2 - a
resultadoFinal = resultado3 / b   

print(f"El resultado final de este super cálculo es: {resultadoFinal}") 
# Jorge -> 617   -  Felipe -> 86.16666666666667  


#* RESUMEN

# INTRO a PYTHON    Multiparadigma (POO, Funciones)  Interpretado            Dinámico  Imperativo (paso a paso)
#                                POO                 Compilado (ejecutable)  Estricto  Declarativo (oculto) 
#                                                  |               Java                |

# Conflictos de versiones -> Entrono Virtual <- Anaconda <- Incorpora librerías y otras herramientas (editor de code)

# VSC -> COMENTARIOS <-> print() - operadores 


#! 2 minutos para que puedan completar la encuesta !!!
#! Q&A

# https://pythontutor.com/
# https://www.w3schools.com/python/default.asp
# https://es.stackoverflow.com/
# https://docs.python.org/3/tutorial/index.html


juju = 23

juju = "wewe"

