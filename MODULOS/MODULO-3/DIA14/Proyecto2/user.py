import validate

def usuario(email, valida_email):
    print("dentro de la funcion usuario")
    is_email = valida_email(email)
    if is_email:
        # print("Tiene formato de email")
        return "Tiene formato de email"
    else:
        # print("NO tiene formato de email")
        return "NO tiene formato de email"
        
if __name__ == "__main__":
    usuario("mau@gmail.com", validate.valida_email)