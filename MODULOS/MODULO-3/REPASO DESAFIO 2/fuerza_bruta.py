import getpass
from string import ascii_lowercase
# abc = "abcdefg" <- ascii_lowercase

abc = ascii_lowercase
# print(ascii_lowercase)
#password = input("Ingrese la contraseña: ").lower() # "ab"
password = getpass.getpass("Ingrese la contraseña: ").lower() # "ab"

contador = 0 

for letra in password:
    print(f"letra -> {letra}") # 
    for caracter in abc:
        contador += 1 
        if letra == caracter:
            break

print(f"La contraseña fue forzada en {contador} intentos")

