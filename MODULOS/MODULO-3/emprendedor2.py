"""
Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados, 
los usuarios normales y los usuarios premium a los cuales se les cobrará una 
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que 
permita considerar el caso recién expuesto. 

Para ello modifica la fórmula de utilidades en la cual se solicite mediante input() 
los parámetros de entrada 
   -  precios de suscripción P, 
   -  usuarios Unormal y 
   -  Upremium y el    <- 50% +
   -  gasto total GT. 
"""


p = float(input('Ingrese el Precio de Suscripción: '))
u = float(input('Ingrese el número de Usuarios Normales: '))
up = float(input('Ingrese el número de Usuarios Premium: '))
gt = float(input('Ingrese los gastos totales: '))

utilidades = (p * u) + (p * up * 1.5) - gt

print(f'Las utilidades son: {utilidades:.2f}')

"""
Precio suscrip. 10
1 Usuario Normal   -> 10 
1 Usuario Premium  -> 15      incrementar 50% 

  10 * 0.5 <-> 5 50% de 10     1 * 10 -> 10  +  0.5 * 10   <-------    1.5 * 10
"""
