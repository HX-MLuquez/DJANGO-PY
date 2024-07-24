
# TODO: *ARGS  ==  TUPLE  == ()

def suma(*dedede):
    print(*dedede)  # 2 3 23 4
    print(type(dedede))  # <class 'tuple'>
    return sum(dedede)


print(suma(2, 3, 23, 4))

"""
2 3 23 4
<class 'tuple'>
32
"""

# TODO:  **KW-ARG  ==  DICT  == {}


def mostrar_kwarg(**kkk):
    print(kkk)  # -> {'edad': 12, 'id': 1, 'nombre': 'Jimy'}
    # print(**kkk) #!ERROR
    print(type(kkk))  # -> <class 'dict'>

    for k, v in kkk.items():
        print(k)


mostrar_kwarg(edad=12, id=1, nombre="Jimy")


print("------------------------------------------")


def get_multiple(diccionario, *claves):
    return {clave: diccionario[clave] for clave in claves}


diccionario_prueba = {'manzana': 'verde',
                      'platano': 'amarillo',
                      'frutilla': 'roja'}
resultado = get_multiple(diccionario_prueba, 'manzana', 'platano')
print(resultado)  # {'manzana': 'verde', 'platano': 'amarillo'}

