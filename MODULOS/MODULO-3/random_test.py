import random 


selected = random.choice(["Ka", "Chi", "Pum"])

print(selected)

number_random = random.randint(1, 100)

print(number_random)

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