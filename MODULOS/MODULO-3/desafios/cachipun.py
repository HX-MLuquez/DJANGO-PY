"""
1. Se pide crear el programa cachipun.py, donde el usuario entregará como
 argumento: piedra, papel o tijera. Para que el computador pueda jugar escogerá un
 valor al azar. Para eso se solicita investigar random.choice() de la librería random.
 (1 Puntos)
 
 La manera en que se ejecutará el programa será de la siguiente manera:
 python cachipun.py piedra
 Tu jugaste Piedra
 Computador jugó tijera
 Ganaste!!
 2. Considerar las opciones de ganar, perder o empatar con la computadora.
 (2 Puntos)
 3. En caso que el argumento sea distinto a piedra, papel o tijera, el programa debe
 mostrar las opciones que se pueden jugar.
 (2 Puntos)
 python cachipun.py papelon
 Argumento inválido: Debe ser piedra, papel o tijera.
"""
import sys
import random

move = sys.argv[1].lower()  # Papel -> papel  or  PAPEL -> papel


if move == "piedra" or move == "papel" or move == "tijera":
    pc = random.choice(['piedra', 'papel', 'tijera'])
    print(f"Tu jugaste {move}.\nComputador jugó {pc}")
    if (move == "piedra" and pc == "tijera") or (move == "tijera" and pc == "papel") or (move == "papel" and pc == "piedra"):
        print('Ganaste!!')
    elif move == pc:
        print('Empate!!')
    else:
        print('Perdiste!!')
else:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")

# print(f' random choice -> {pc}')
# print(f' move -> {move}')

# -> piedra   otro caso -> pepe
if move != "piedra" and move != "papel" and move != "tijera":
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
else:
    pc = random.choice()
    print(f"Tu jugaste {move}.\nComputador jugó {pc}")
    if (move == "piedra" and pc == "tijera") or (move == "tijera" and pc == "papel") or (move == "papel" and pc == "piedra"):
        print('Ganaste!!')
    elif move == pc:
        print('Empate!!')
    else:
        print('Perdiste!!')
