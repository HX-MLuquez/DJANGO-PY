
from masa import cambiar_masa
from salsa import cambiar_salsa
from mostrar import mostrar_ingredientes
from agregar import agregar_ingrediente
from eliminar import eliminar_ingredientes

import os 
import time

ingredientes_orden = {'masa': 'Masa Tradicional',
                      'salsa': 'Salsa de Tomate',
                      'ingredientes': ['Queso']
                      }

# print(f'Su orden es de pizza con {ingredientes_orden["masa"]}, {ingredientes_orden["salsa"]} y los ingredientes {ingredientes_orden["ingredientes"]}')


while True:
    # exit()
    os.system('clear')
    opcion = input("""¿Qué desea ordenar? 
                   1. Seleccionar tipo de Masa
                   2. Seleccionar tipo de Salsa
                   3. Mostrar ingredientes
                   4. Agregar ingredientes
                   5. Eliminar ingredientes
                   6. Ordenar pizza 
                   Otro. Cancelar pedido
                   """)
    if opcion == "1":
        nuevos_ingredientes = cambiar_masa(ingredientes_orden)

        ingredientes_orden = nuevos_ingredientes

        print(ingredientes_orden)
       
    elif opcion == "2":
        nuevos_ingredientes = cambiar_salsa(ingredientes_orden)

        ingredientes_orden = nuevos_ingredientes

        print(ingredientes_orden)
       
    elif opcion == "3":
        
        mostrar_ingredientes(ingredientes_orden)
        time.sleep(3)
    elif opcion == "4": # AGREGAR INGREDIENTES
        seleccionado = int(input("""Seleccione su ingrediente:
                                    1. Aceituna
                                    2. Ananá
                                    3. Palmito
                                    4. Jamón
                                    """))
        agregar_ingrediente(ingredientes_orden, seleccionado)
        time.sleep(3)
    elif opcion == "5": # ELIMINAR INGREDIENTES
        eliminar_ingredientes(ingredientes_orden)
    elif opcion == "6": # PEDIDO
        exit()
        
