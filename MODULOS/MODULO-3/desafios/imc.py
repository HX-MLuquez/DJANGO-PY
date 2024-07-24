# print("hola")

"""
Actividad 1 - IMC
 Se solicita crear el programa imc.py que permita calcular el IMC de una persona.
 1. Al programa se debe ingresar el peso en Kg y la talla (altura) en centímetros.
 (1 Puntos)
 2. Calcular el IMC ajustando los valores de entrada a las unidades requeridas por la
 fórmula. El resultado se debe informar con 2 decimales.
 (2 Puntos)
 3. Entregar al usuario una salida acorde que permita conocer el valor de su IMC
 además de la clasificación dada por la OMS.
 (2 Puntos)
 A modo de validación se entregan los siguientes valores para revisar su código:
 
 sys.argv[    0    1     2  ]
 -> python imc.py "81" "178" <- input
 
 output -> Su IMC es 25.56
           La clasificación OMS es Sobrepeso
           
           Su IMC es 40.16
           La clasificación OMS es Obesidad Grado III
"""
import sys 
peso = float(sys.argv[1])
altura = float(sys.argv[2])

print(f'peso -> {peso} y altura -> {altura/100}')
resultado = peso/(altura/100)**2

print(f'resultado -> {resultado:.2f}')

"""
 IMC     Clasificación OMS
 < 18.5          Bajo Peso
 [ 18.5, 25 [    Adecuado
 [ 25, 30 [     Sobrepeso
 [ 30, 35[      Obesidad Grado I
 [ 35, 40 [     Obesidad Grado II
 > 40           Obesidad Grado III
"""
mensaje = "No ha entrado"
if resultado < 18.5:
    mensaje = "Bajo Peso"    
# print(f'mensaje -> {mensaje}')
elif resultado < 25:
    mensaje = "Adecuado"
elif resultado < 30:
    mensaje = "Sobrepeso"
elif resultado < 35:
    mensaje = "Obesidad Grado I"
elif resultado < 40:
    mensaje = "Obesidad Grado II"
else:
    mensaje = "Obesidad Grado III"
    
print(f'Su IMC es {resultado:.2f}\nLa clasificación OMS es {mensaje}')