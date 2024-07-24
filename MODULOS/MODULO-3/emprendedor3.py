"""
Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula 
original de utilidades donde el usuario ingrese el precio de suscripción P, el número de 
usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del año 
anterior Uanterior, todo esto mediante input(). El programa debe calcular las utilidades 
actuales y mostrar la razón entre las utilidades actuales y las del año anterior con dos 
decimales. 
"""


p = float(input('Ingrese el Precio de Suscripción: '))
u = float(input('Ingrese el número de Usuarios: '))
gt = float(input('Ingrese los gastos totales: '))

ua = float(input('Ingrese las utilidades del año anterior: '))
utilidades = p * u -gt

reason= utilidades / ua

print(f'Las utilidades son: {utilidades:.2f}')
print(f'La razón de las utilidades actuales con las del año anterior son: {reason:.2f}')


# Tipos de Datos
# Number   INT  FLOAT
# BOOLEAN
# STRING