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

nombre = input('Ingrese su nombre: ')
edad = input('¿Qué edad tienes? ')
ocupacion = input('¿Cuál es tu ocupación? ')
lugar_de_trabajo = input('Ingrese su lugar de trabajo: ')
caracteristica1 = input('Ingrese 3 características:\n1. > ')
caracteristica2 = input('2. > ')
caracteristica3 = input('3. > ')
pasatiempo1 = input('Ingrese 2 pasatiempos:\n1. > ')
pasatiempo2 = input('2. > ')
algo_que_hacer = input('¿Qué quieres hacer? ')

print(f'''Mi nombre es {nombre}, tengo {edad} años y me desempeño como {ocupacion} en {lugar_de_trabajo}.
Soy {caracteristica1}, {caracteristica2} y {caracteristica3}.
Mis pasatiempos preferidos son {pasatiempo1} y {pasatiempo2} y me gustaría {algo_que_hacer}.''')
