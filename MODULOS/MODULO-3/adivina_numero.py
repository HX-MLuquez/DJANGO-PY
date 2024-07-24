import random

# Actividad: Juego de Adivinanza de Números
# Instrucciones:
# 1. Crea un programa llamado adivina_numero.py.
# 2. El programa debe generar un número aleatorio entre 1 y 100.
# 3. El usuario tiene exactamente 3 intentos para adivinar el número.
# 4. Después de cada intento, el programa debe decirle al usuario si el número adivinado es muy alto, 
# muy bajo o correcto.
# 5. Si el usuario adivina el número correctamente, el programa debe felicitarlo y terminar.
# 6. Si el usuario no adivina el número en los intentos permitidos, el programa debe revelar el número y terminar.
# Requerimientos: Utiliza las siguientes funciones y conceptos de Python: 
# input(), print(), if, elif, else, random, sys.argv (si así lo prefieres), ceil, float, y operaciones aritméticas simples,
# solamente lo aprendido hasta el momento en cuanto a lenguaje.


aleatorio = random.randint(1,100) # 32
print(aleatorio)
print("Este computador generó un número del 1 al 100, tienes 3 intentos para acertar !!!")

valor = int(input("\nIngresa el 1° valor >")) # 32

if valor > aleatorio:
    print("El número es menor, vamos que se puede!!!")
    valor = int(input("Ingresa el 2° valor >"))
elif valor < aleatorio:
    print("El número es mayor, vamos que se puede!!!")
    valor = int(input("Ingresa el 2° valor >"))
elif valor == aleatorio:
    print("Grandioso adivinaste!!!")  

if valor > aleatorio:
    print("El número es menor, vamos que se puede!!!")
    valor = int(input("Ingresa el 3° valor >"))
elif valor < aleatorio:
    print("El número es mayor, vamos que se puede!!!")
    valor = int(input("Ingresa el 3° valor >"))
elif valor == aleatorio:
    print("Grandioso adivinaste!!!")     

if valor == aleatorio:
    print("Grandioso adivinaste!!!")     
else:
    print("Perdiste, juega en otra oportunidad!!!")

