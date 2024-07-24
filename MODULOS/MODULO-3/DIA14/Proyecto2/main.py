
import user 
import validate

def padre():
    email = input("Ingrese su email: ")
    mensaje = user.usuario(email, validate.valida_email)
    print(mensaje)
    
padre()
    

"""
* DOCUMENTAR

* USAR +++ PRINT

* DEFINIR en cada ETAPA ¿? que ENTRA IN
                      * ¿? que SALE
"""