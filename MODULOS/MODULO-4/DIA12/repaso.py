

# todo_ Manejo de ERRORES
#    _______________
#   |               |
# * TRY - EXCEPT - ELSE - FINALLY       RAISE -> Fuerza una EXCEPTION


swap = True


def div(a, b):
    try:
        if b != 2:
            print("si")
            raise TypeError("este es el mensaje creado al armar la instancia ....") #! FORZAR ERROR
        else:
            print("no")
        resultado = a/b
       
    # except Exception as e:
    #     print(f"En error general -> {e}")
    #     print("atrapo todos los errores")
    except ZeroDivisionError as z:
        print(f"En error ZeroDivisionError {z}")
    except TypeError as ty:
        print(f"En error TypeError ::: {ty}")
    else:
        print("Si entra el TRY entra el ELSE")
    finally:
        print("siempre se ejecuta")


# print(div(10, 2))
print(div(10, 2))


with open("ruta.log", 'r') as archivo:
    archivo.read()

# Puntero pos 0 -> 10 -> 20  -> 30
with open("ruta.log", 'r') as archivo:
    linea = archivo.readline()
    # linea2 = archivo.readline()
    # linea3 = archivo.readline()
    while linea:
        # sasasasa
        linea = archivo.readline()

with open("ruta.log", 'w') as archivo: # 
    archivo.write("holis")
    
with open("ruta.log", 'a+') as archivo: # 
    # El puntero está en el final 
    archivo.seek(0) #* PUNTERO
    archivo.read()

