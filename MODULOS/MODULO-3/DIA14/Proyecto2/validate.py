def valida_email(email):
    """Esta función valida que el tipo de email sea válido e ...
    Params:
        email: [string] [description]
    Return:
        boolean
    """
    print("Dentro de VALIDAR")
    arroba = False
    for t in email:
        print(f'--> {t}')
        if t == "@":
            print("entra en la condicion de valida")
            arroba = True
            break
    return arroba

if __name__ == "__main__":
    valida_email("hola.com")

