import sys
import time
# int() <-> STRING de entrada lo debemos en este caso pasar a número
i = int(sys.argv[1])
# qué es i??? <- es una variable, y ese es su nombre
print(f"--> {i}")

while i >= 0: # CORTE cuando i == 0
    print(i)
    time.sleep(1) # time.sleep(1) detiene (PAUSE) el code durante 1 SEG.
    i -= 1 # Toma la variable i y la decrementa en 1 <- i = i - 1
    # print(i)
    if i == -1:
        print('Mensaje CLAVE')

print("BOOM!") # al salir del ciclo la bomba explota!
"""
SYS es un Módulo que usamos el método .argv (argumentos)
sys.argv["x"] <- input mediante el escrito del script
python bomba.py Pepe
"""
