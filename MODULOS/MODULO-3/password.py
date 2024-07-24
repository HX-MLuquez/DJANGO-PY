import getpass
#* Crear un programa donde el usuario debe ingresar un password en la plataforma
# debe tener 6 o mas caracteres y debe ser correcto
real_pass = "123456"
# password = input("Ingrese su password > ")
password = getpass.getpass("Ingrese su password > ") # ooooo (me deja escribir por consola y lo mantiene oculto)
error = False

if len(password) < 6:
    # print("El password debe contener al menos 6 caracteres")
    error = "El password debe contener al menos 6 caracteres"
elif password != real_pass:
    # print("Password incorrecto")
    error = "El password debe contener al menos 6 caracteres"
else:
    print("Inicio Exitoso")


if error: # True
    print(error)
