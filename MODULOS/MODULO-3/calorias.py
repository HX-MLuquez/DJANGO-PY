import math

proteina = float(input("Ingrese los gr de proteina:\n>"))
carbo = float(input("Ingrese el los de Carbohidrato:\n>"))
grasa = float(input("Ingrese el los de Grasa:\n>"))

calorias = 4 * (proteina + carbo) + 9 * grasa

#  calorias = (4 * proteina) + (4 * carbo) + (9 * grasa)


print(f'Las calorías totales del producto son: {math.ceil(calorias)}') # redondeo hacia arriba

"""
1 min de cierre para llenar la encuesta
https://forms.gle/pPieF2iRd4vqsjcS9
"""