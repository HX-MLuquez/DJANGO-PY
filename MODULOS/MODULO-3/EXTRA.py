"""
Actividad: Juego de Adivinanza de Números
Instrucciones:
1. Crea un programa llamado adivina_numero.py.
2. El programa debe generar un número aleatorio entre 1 y 100.
3. El usuario tiene exactamente 3 intentos para adivinar el número.
4. Después de cada intento, el programa debe decirle al usuario si el número adivinado es muy alto, 
muy bajo o correcto.
5. Si el usuario adivina el número correctamente, el programa debe felicitarlo y terminar.
6. Si el usuario no adivina el número en los intentos permitidos, el programa debe revelar el número y terminar.

Requerimientos: Utiliza las siguientes funciones y conceptos de Python: 
input(), print(), if, elif, else, random, sys.argv (si así lo prefieres), ceil, float, y operaciones aritméticas simples,
solamente lo aprendido hasta el momento en cuanto a lenguaje.
"""

import random

print("Bienvenidos a Adivina Número!!!\nTienes hasta 3 intentos para adivinar :-)")
# Generar un número aleatorio entre 1 y 100
number_ale = random.randint(1, 100)
print(f'numero aleatorio -> {number_ale}')
message_win = f'Has acertado, el número seleccionado {number_ale} es el correcto\nFelicidades!!!'
message_lose = 'No lo has conseguido, si quieres puedes volver a jugar'
number_max = 'El número seleccionado es MAYOR al número al que debes acertar'
number_min= 'El número seleccionado es MENOR al número al que debes acertar'

number = int(input(
    "Este es tu primer intento, Escribe un número entre el 1 y el 100\n > "))
if number == number_ale:
    print(message_win)
elif number > number_ale:
    number = int(input(f'{number_max}\nHas tu segundo intento > '))
    if number == number_ale:
        print(message_win)
    elif number > number_ale:
        number = int(input(f'{number_max}\nHas tu tercer intento > '))
        if number == number_ale:
            print(message_win)
        else:
            print(message_lose)
    else:
        number = int(input(f'{number_min}\nHas tu tercer intento > '))
        if number == number_ale:
            print(message_win)
        else:
            print(message_lose)
else:
    number = int(input(f'{number_min}\nHas tu segundo intento > '))
    if number == number_ale:
        print(message_win)
    elif number > number_ale:
        number = int(input(f'{number_max}\nHas tu tercer intento > '))
        if number == number_ale:
            print(message_win)
        else:
            print(message_lose)
    else:
        number = int(input(f'{number_min}\nHas tu tercer intento > '))
        if number == number_ale:
            print(message_win)
        else:
            print(message_lose)
