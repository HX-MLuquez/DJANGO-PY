import sumar 
import restar 
from datos import tomar_datos
from continua import sigue_o_no
import os
import time

calculando = True

while calculando:
    os.system('clear')
    opcion = input("""Calculadora:
                ¿Que operación vas a realizar?
                1. Sumar
                2. Restar
                0. Salir
                """)

    if opcion == "1":
        a,b = tomar_datos()
        print(sumar.suma(a,b))
        calculando = sigue_o_no()
        time.sleep(3)
        
    elif opcion == "2":
        a,b = tomar_datos()
        print(restar.resta(a,b))
        calculando = sigue_o_no()
        time.sleep(3)
        
    elif opcion == "0":
        print("Chau")
        # calculando = False
        time.sleep(3)
        exit()
        
    else:
        print("Operador inválido")
        calculando = False

    # print(restar.resta(8,8))
    # print(sumar.suma(8,8))