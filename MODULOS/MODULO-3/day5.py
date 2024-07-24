# {{{{{{{{{{{}}}}}}}}}}}
# [[[[[[[[[[[]]]]]]]]]]]

edad = 43  # Un solo = es para asignar un valor

# TODO: OPERADORES de COMPARACIÓN

print(edad == 43)  # True # Doble igual == es para comparar
print(edad != 43)  # False
print("------------")
print(12 > 43)  # False
print(12 >= 12)  # True
print(1 < 432)  # True
print(12 <= 43)  # True

# Ejercicio

nombre = "Juan"
edad = 27  # años
n_hijos = 0
graduacion_colegio = 17  # años duracion_uni = 6 # años
duracion_pololeo = 3  # años
exp_laboral = 4  # años
print("------ Ejercicio -----")

# ¿Juan es mayor de edad?
print(edad >= 18)  # True

# ¿Juan se graduó del colegio antes de los 18 años?
print(graduacion_colegio <= 17)  # True

# ¿Juan no tiene 4 años de experiencia laboral?
#         4 es difernte a 4 ?
print(exp_laboral != 4)  # False

# ¿Juan tiene hijos?
#       0  es diferente a 0
# print(n_hijos == 0) # True  <-> != <->  False
print(n_hijos != 0)  # False

# ¿Juan no tiene hijos?
print(n_hijos == 0)  # True


"""
Para preguntar si “algo es igual”, 
se utiliza doble signo igual (==). 
Ten en cuenta que utilizar 
sólo un signo igual implica una 
asignación, es decir, definir una 
variable, lo cual no devuelve un 
valor True o False
"""
print("-------------- Preguntas indirectas -----------------")
nombre = "Juan"
edad = 27  # años
n_hijos = 0
graduacion_colegio = 17  #
duracion_uni = 6  # años
duracion_pololeo = 3  # años
exp_laboral = 4  # años


# * Preguntas indirectas

# Juan con 23 terminó la uni
# ¿Al graduarse de la Universidad ya había cumplido 22?

edad_termino_uni = graduacion_colegio + duracion_uni
print(f'Juan ya había cumplido 22 al graduarse en la uni: {edad_termino_uni >= 22}')

# ¿Juan comenzó a pololear a los 25?
# Sabemos que Juan inicia su pololeo a los 24
edad_inicio_pololeo = edad - duracion_pololeo
print(f'Juan comenzó a pololear a los 25? {edad_inicio_pololeo == 25}')
# print(f'Juan comenzó a pololear a los 25? {edad_inicio_pololeo >= 25}')

# ¿Juan lleva más tiempo trabajando que estudiando (uni)? # ¿Juan tiene más tiempo trabajando?

print(f'¿Juan lleva más tiempo trabajando que estudiando (uni)? {exp_laboral > duracion_uni}')


nombre = "Juan"
me_llamo_juan = nombre == "Juan"
# me_llamo_juan = True
print(f'que es me_llamo_juan ¿? {me_llamo_juan}')

print(type(me_llamo_juan))  # Me informa el tipo de datos que es -> BOOLEAN

"""
XOR (^)
alt gr + { { 
alt + 94  <- ASCII
"""
nombre = "Juan"
edad = 27  # años
n_hijos = 0
graduacion_colegio = 17  #
duracion_uni = 6  # años
duracion_pololeo = 3  # años
exp_laboral = 4  # años
print("-------------- Operadores Lógicos -----------------")
# TODO: Operadores Lógicos

# AND <->  and    ("Y")
# OR  <->  or     ("O")
# XOR <->  ^      ("Ooo") # True True False

# ¿Juan es mayor de edad y está pololeando?
# Implementamos Operador lógico AND + Operador de comparación >
print(edad > 18 and duracion_pololeo > 0)  # True


# ¿Puede Juan postular?
print("---------XOR ERROR---------")
#           True             False
print(duracion_uni >= 6)  # True
print(exp_laboral > 5)  # False
#          True       XOR     False
print(duracion_uni >= 6 ^ exp_laboral > 5)  # True #! False

print("------------------")

print(duracion_uni >= 6 or exp_laboral > 5)  # True

menor_28 = edad < 28  # True
exp_menor_3 = exp_laboral < 3  # False
#       True  XOR   False
print(menor_28 ^ exp_menor_3)  # True

#! SOLUCIÓN XOR al comparar datos complejos de utilizar ()
print((duracion_uni >= 6) ^ (exp_laboral > 5))

print("--------RESUMEN----------")
# TODO: RESUMEN

# Operadores de Comparación:
l= 23 == 21 # False
m= 12 != 2 # True
n= 34 > 21 # True
o= 234 >= 432 # False
p= 4 < 12 # True
q= 123 <= 987 # True

# Operadores lógicos: and, or y ^
print(m and o and p) # False 
print(q or n or l) # True
print((m ^ n ^ p)) # True #! ->  False

print((m and n) or l) # True
