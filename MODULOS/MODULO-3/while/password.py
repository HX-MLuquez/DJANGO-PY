import getpass  # getpass.getpass -> input OCULTO

password_new = getpass.getpass("Ingrese la clave secreta > ")
# print(f'password is: {password_new}')

while password_new != "hola mundo": # True -> False
    #* CASO BASE - CORTE
    password_new = getpass.getpass(f"Clave {password_new} Incorrecta\nIngrese de nuevo la clave secreta > ")

print(f'Clave secreta {password_new} correcta!!!') 

