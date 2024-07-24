# FUNCTION
nombre = "Pepe"


def mi_funcion():
    print("hola funciones")


print(mi_funcion)  # <function mi_funcion at 0x0000027DBDC6A340>
print(type(mi_funcion))  # <class 'function'>

# mi_funcion() <- INVOCAR / LLAMAR / EJECUTAR
print(mi_funcion())  # ! Ejecuta e Imprime lo que retorna <- None


def mi_funcion2():
    print("hola funciones")
    return "hola mundo"


print(mi_funcion2())  # ! Ejecuta e Imprime lo que retorna <- "hola mundo"

# TODO: Dame el valor de lo que retorna la invocación de esta función
result = mi_funcion2()
print(f'-> {result}')  # -> "hola mundo"


print("---------------- area_rect --------------------------")


def area_rect(lado_a, lado_b):  # PARÁMETROS / NOMBRES de var
    print(f'verificamos si nos pasan valor del 1° parámetro -> {lado_a}')
    resultado = lado_a * lado_b
    return resultado


area_rect(12, 2)  # ARGUMENTOS / VALORES
print(area_rect(5, 3))  # Ejecuto y obtengo el return

print("---------------- area_rect2 --------------------------")


def area_rect2(lado_a, lado_b):  # PARÁMETROS / NOMBRES de var
    print(f'verificamos si nos pasan valor del 1° parámetro -> {lado_a}')
    resultado = lado_a * lado_b

    def sum(a, b):
        return a+b
    
    if resultado == 15:
        return sum
    else:
        return resultado


guardar = area_rect2(5, 3)  # -> return sum -> def sum(a, b):return a+b
print(guardar(2,4))  # Ejecuto y obtengo el return
