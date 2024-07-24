# Todo: TIPOS de DATOS

# * Valores Numéricos

# * ENTERO - INT  ||  DECIMALES - FLOAT

# * INTEGER
num_int_1 = 21
print(num_int_1)
print(302)
print(3+7)
print(-35)

# * FLOAT
# estos son valores float
print(27.6)
print(27/2)  # -> 13.5
print(-277.6232)

print(3.5 + 12)
print(20 * 45.6)


# * STRINGS

print('Comillas simples')
print("Comillas dobles")
print('"Comillas dentro de otras comillas"')
print("'Comillas dentro de otras comillas'")

# print("Comillas dobles y "algo" mas") #! ERROR por usar comillas dobles dentro de comillas dobles
"""
 print("Comillas dobles y "algo" mas")
          ^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
"""


#! IMPORTANTE - DIFERENCIAR Tipo de texto  Number dentro de String o Number simplemente
print("NUMBER")
print(143)
print(143 + 88)  # -> 231
print("NUMBER en STRING")
print("143")
# -> 14388 <- "14388" <- devuelve un string resultado de una concatenación de strings
print("143"+"88")


# * Concatenación (SUMAR)
print("Carlos" + "Santana")  # CarlosSantana
print("Carlos " + "Santana")  # Carlos Santana

# * Concatenación
print("15" + "23")  # esto resulta en 1523


# * Concatenación (multiplicar)
print("Fer " * 8)  # -> Fer Fer Fer Fer Fer Fer Fer Fer
print(5 * "Juan")  # -> JuanJuanJuanJuanJuan

# TODO: Métodos
# * .count() | Nos devuelve la cantidad de veces que aparece un subString .count("p") dentro de un string "pepito"
print("pepito".count("p"))  # -> 2
print("pepito".count("a"))  # -> 0
print("pepito".count("pe"))  # -> 1

# * .upper() | todo a MAYÚSCULA
print("Walter".upper())  # -> WALTER

# * .lower() | todo a minúscula
print("Pilín".lower())  # -> pilín

print("carlos santana".title()) # Carlos Santana
# resulta en Carlos Santana

# * len("He aquí la primera ...")

# -> 22 <- caracteres contiene este string
print(len("He aquí la primera ..."))


# * .join()   |  le pasamos por params una lista de elementos y antes del .join el caracter que funciona de unión
# entra una lista ["a", "b", "c"] ->   "a b c"
# -> entra lista ["a", "b", "c"] -> sale un string  "a, b, c"
print(", ".join(["a", "b", "c"]))

# -> entra lista ["a", "b", "c"] -> sale un string  "a&&b&&c"
print("&&".join(["a", "b", "c"]))


# * Salto de Línea

print("En un lugar de la mancha,\nnunca me acuerdo como sigue,\npero si muy bien creo de que trata")


# * Valores booleanos

# True || False
print(True)
print(False)

# Todo: VARIABLES

# * NOMBRE <-> VALOR   ||   KEY <-> VALOR

animal1 = "Lobo"
animal2 = "Loro"

# 3animal = "Perro" #! Error  por que no puede contener un número al inicio
# animal otro = "Gato" #! Error por que no puede contener espacios el nombre de la variable

products = ""

cant_products = 23
cant_people = 32
number_people_square_meter = 101

# * Tipos de datos
# Una variable poseerá un tipo de dato asociado, según el valor que se le asigne, donde los
# tipos de datos pueden ser, entre otros, integer, string, float o bool
decimal1 = 54.8
texto2 = "hola"
swap = True
print(type(cant_products))  # -> <class 'int'> <- INT
print(type(decimal1))  # -> <class 'float'> <- FLOAT
print(type(texto2))  # -> <class 'str'> <- STRING
print(type(swap))  # -> <class 'bool'> <- BOOLEAN


# Ejercicios

z = "Ju "
z = z * 4
print(z)

title1 = "Bienvenidos a: "
title2 = "PYTHON que no es MONTY"
print(title1 + title2)


# TODO: Transformando los datos

# * Interpolación
# Permite introducir una variable, un dato o una operación válida dentro un String.

print("El título es: ", title2)

# * FORMAT (f)
print("El título es: {}".format(title2))
print("El título es: {} {}".format(title1, title2))

print(f"El título ahora con el format más cool es: {title2}")


# * Precisión de datos (recortar cantidad de decimales a mostrar)

# Operación que arroja varios decimales
print(f'El resultado es {1/9}')  # -> 0.1111111111111111

# Muestro sólo 2 decimales
result = 1/9
print(f'El resultado es: {result:.2f}')  # -> 0.11 # FLOAT .00  -> :.1f   .0

# Todo: Ingresando datos

# * input()
# * cuadro de diálogo que permite al usuario ingresar texto
# * Entra un STRING

# nombre_propio = input('Ingrese su nombre: ')
# # edad = 37 # Number
# edad = input('Ingrese su edad: ')  # "37"

# print(f'Mi nombre es {nombre_propio} y tengo {edad} años')


# edad_number_input = float(input('Ingrese de nuevo su edad: '))  # -> number 23.0
# print(f'es el input string de edad pasado a number -> {edad_number_input}') # -> 23.0


# * EJERCICIO GUIADO

# 1. Lectura clara y profunda de la consigna
# 2. Uso de la platilla
"""
Mi nombre es Bill, tengo 52 años y me desempeño como CEO en Microsoft.
Soy Creativo, Apasionado y Visionario.
Mi pasatiempo es jugar Golf y me gustaría poder jubilarme pronto.
"""

# 3. Definir los aspectos a automatizar (a cambiar), y son:
# * Nombre, Edad, Ocupación, Lugar de Trabajo, Características, Pasatiempos, Algo que hacer

# nombre
# edad
# ocupacion
# lugar_de_trabajo
# caracteristica1
# caracteristica2
# caracteristica3
# pasatiempo1
# pasatiempo2
# algo_que_hacer

# print(f'')


# * Tipos de Datos Nativos de Python
"""
Numbers 
Strings
Booleans
"""

# * Métodos

"""
.count()
.upper()
.lower()
.join()
.title()

len()
"""

# * print()  -  input() <- propmt


print("------------------ Operadores y librerías -------------------")

# * OPERADORES - Matemáticos || Comparación || Lógicos

# * Matemáticos

print(5/2)  # -> 2.5
print(5//2)  # devuelve el resultado en entero -> 2

print(5 % 2)  # el resto (módulo) -> 1

print(2 ** 3)  # 2 elevado a la 3 -> 8

# * PRECEDENCIA  |  Resuelve primero | ** raiz  |  div y mult   | sum y resta

print(4 - 2 * 5)
#   4 - 10 = -6

print((4 - 2) * 5)
#    2 * 5 = 10

print("------------ TEST BOOLEAN result --------------")
print("2 es igual a 2 -> ", 2 == 2)  # True
print("2 es igual a '2' -> ", 2 == "2")  # False

print("calculo 4+3 es igual a 7", 3 + 4 == 7) # True


