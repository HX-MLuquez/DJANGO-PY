

def multiplicar(a, b):
    return a * b


def mult_mas_suma(a, b, c, func_mult):
    return func_mult(a, b) + c

print(f'---> {mult_mas_suma(2,3,6,multiplicar)}')

# multiplicar(8) #!TypeError: multiplicar() missing 1 required positional argument: 'b'


print(multiplicar(4, 3))  # ! IMPORTANTE IMPRIMIMOS lo que está luego del RETURN


usuarios = [{"id": 12, "nombre": "Jimy", "email": "dede@gmail.com"}, {"id": 23, "nombre": "Pepe",
                                                                      "email": "pepe@gmail.com"}, {"id": 2, "nombre": "John", "email": "john@gmail.com"}]

#                          []   ,      "Jojo"


def busca_usuario(lista_usuarios, nombre_usuario):
    for user in lista_usuarios:
        if user["nombre"].lower() == nombre_usuario.lower():
            print(f'El usuario {
                  nombre_usuario} si se encuantra en la lista de invitados')
            return
    print(f'El usuario {nombre_usuario} No se encuantra en la lista')


busca_usuario(usuarios, "Jimo")
