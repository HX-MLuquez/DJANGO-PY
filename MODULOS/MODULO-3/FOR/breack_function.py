

# TODO: BREACK

# * LIST
perros = ["doberman", "dogman", "boby"]
buscar = input("Ingrese perro: ")

for perro in perros:
    print(perro)
    if buscar == "doberman":
        break  # Cuando este se ejecuta el CICLO se termina

print("Fin del CODE")

# * STRING

texto = "mau@hotmail.com"
arroba = False
for t in texto:
    print(f'--> {t}')
    if t == "@":
        arroba = True
        break  # Cuando este se ejecuta el CICLO se termina

if arroba:
    print("Tiene formato de email")
else:
    print("NO tiene formato de email")

print("-----------------------------------------")


def valida_email(email):
    """Esta función valida que el tipo de email sea válido e ...
    Params:
        email: [string] [description]
    Return:
        boolean
    """
    arroba = False
    for t in email:
        print(f'--> {t}')
        if t == "@":
            arroba = True
            break
    return arroba


def usuario(email):
    is_email = valida_email(email)
    if is_email:
        print("Tiene formato de email")
    else:
        print("NO tiene formato de email")
