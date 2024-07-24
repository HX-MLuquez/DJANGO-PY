import time

evento = False 
mensaje = "Nada"

while not evento: # not False <-> True   /  not True <-> False
    print("hola")
    time.sleep(1) # detiene en esta línea 1 SEG
    print("mundo")
    # Agregar un input que valide (condición IF) ser "Lopez" para activar el caso corte
    mensaje = input("Ingrese su apellido > ")
    if mensaje == "Lopez":    
        evento = True # Esto finaliza el ciclo

print("Fin del ciclo")

"""
evento= False
while not evento:
    print("Resultad1")
    # evento = False
    print("Infinito ")
    
print("Fin")
"""


#TODO: PLEASE -> COMPLETE -> https://forms.gle/avKKrqnBXbKdRSVs8