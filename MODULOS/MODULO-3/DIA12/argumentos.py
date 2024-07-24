import sys 
import getpass
# print("hola")

nombre = sys.argv[1]
apellido = sys.argv[2]

print(type(sys.argv)) # list

print(f"Mi nombre es {nombre}") 
print(f"Mi apellido es {apellido}") 
print(f"Nombre de este archivo es {sys.argv[0]}") 


entrada = input("Usuario: ")
password = getpass.getpass("Contraseña: ")

print(entrada, password)