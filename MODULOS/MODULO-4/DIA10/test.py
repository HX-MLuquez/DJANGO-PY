

# print("hola" #! SyntaxError: incomplete input


# todo_  EXCEPCIONES - las podemos manejar
num = int(input("Ingrese número: "))  # ! <- ingreso "we" <- ValueError:

print(num)
print("Hola Mundo")


print(nanana)

print("Hola Mundo de nuevo")  # ! NameError: name 'nanana' is not defined


resultado = 12 + nununu
print(resultado)
print("hola")
print("ERROR")

try:
    resultado = 12 / 0
    print(resultado)
    print("hola")
except:
    print("ERROR NameError")
    print("hola luego del error")


try:
    resultado = 12 / 0
    print(resultado)
    print("hola")
except:
    print("ERROR NameError")
    print("hola luego del error")
except ZeroDivisionError:  # ! except clause cannot appear after catch-all except
    print("ERROR ZeroDivisionError")
    print("hola luego del error")


print("Continúa")


try:
    resultado = 12 / 0
    print(resultado)
    print("hola")
except NameError:
    print("ERROR NameError")
    print("hola luego del error")
except ZeroDivisionError:
    print("ERROR ZeroDivisionError")
    print("hola luego del error")


print("Continúa")


consultar = True
while consultar:
    try:
        edad = int(input("Ingrese su edad:\n"))
        consultar = False
    except ValueError:
        print("Debe ingresar un número")

print("fuera del bucle")


consultar = True
while consultar:
    try:
        num2 = int(input("Ingrese un número mayor a cero: "))
        resultado = 12 / num2
        print(resultado)
        consultar = False
    except ValueError:
        print("Tipo de valor ingresado incorrecto")
    # except ZeroDivisionError:
    #     print("No se puede dividir por cero")
    except Exception as e:
        # * Error en Exception: division by zero
        print(f'Error en Exception: {e}')
    print("Continúa intentando: ")
print("FIN")


# swap = True

while True:
    try:
        edad = int(input("Ingrese edad: "))
        if edad < 18:
            raise ZeroDivisionError("Debes ser mayor de edad")
        print("Puedes pasar")
        break
    except ValueError:
        print("dentro de ValueError")
    except ZeroDivisionError:
        print("dentro de ZeroDivisionError")
    except Exception as e:
        print(f"Error en Exception -> {e}")

print("FIN")


class Error(Exception):
    pass


class EdadError(Error):
    def __init__(self, mensaje, edad) -> None:
        self.mensaje = mensaje
        self.edad = edad


try:
    edad = int(input("Ingrese su edad: "))
    if edad < 18:
        raise EdadError("La edad es incorrecta.", edad)
except ValueError:
    print("El valor es incorrecto")
except EdadError as e:
    print(
        f'En mi clase EdadError el error es -> {e.mensaje} y el valor ingresado es {e.edad}')

print("Y CONTINUA PYTHON")
# class AlturaError(Exception):
#     def __init__(self, mensaje, altura) -> None:
#         super().__init__(mensaje)
#         self.edad = altura


# todo_ Finally

class Error(Exception):
    pass


class EdadError(Error):
    def __init__(self, mensaje, edad) -> None:
        self.mensaje = mensaje
        self.edad = edad

intentos = 0
while intentos <= 3:
    try:
        edad = int(input("Ingrese su edad:\n"))
        if edad < 0:
            raise EdadError("Debe ser un N° positivo.", edad)
        divisor = int(input("Ingrese número para dividir su edad:\n"))
        print(edad / divisor)
    except ValueError:
        print("Debe ingresar un número")
    except ZeroDivisionError:
        print("El N° por el cual desea dividir no puede ser cero")
    except EdadError as e:
        print(f"La edad '{e.edad}' no es válida. {e.mensaje}")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        print("Dentro del bloque que siempre se ejecuta")
        intentos += 1
