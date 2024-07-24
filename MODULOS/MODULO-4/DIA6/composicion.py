
# todo_ Composición o Agregación fuerte - hay DEPENDENCIA
class Motor:
    def arrancar(self):
        print("El motor se ha encendido")


class Coche:
    def __init__(self) -> None:
        self.motor = Motor()

    def encender(self):
        self.motor.arrancar()
        print("El coche está listo")
        otro_motor = Motor()
        otro_motor.arrancar()


coche1 = Coche()  # < Object   <Object1> >
coche1.encender()  # < Object   <Object1 - self.motor> <Object2 - otro_motor> >

# del coche1
# print(coche1)

print("\n--------------------------\n")


class Producto:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    def saludar(self):
        return "Buenas soy una fruta o una verdura"


producto1 = Producto("papa")
print(producto1.nombre)

producto2 = Producto("tomate")
producto3 = Producto("limón")
# _Producto__nombre


class Productos:
    def __init__(self) -> None:
        self.lista_de_productos = []

    def agregar_producto(self, producto: Producto):
        self.lista_de_productos.append(producto)


verduleria1 = Productos()
verduleria1.agregar_producto(producto1)
verduleria1.agregar_producto(producto2)
verduleria1.agregar_producto(producto3)

print(verduleria1.lista_de_productos)
# [ <__main__.Producto object at 0x0000027915F7B3B0>,
#   <__main__.Producto object at 0x0000027915F7B770>,
#   <__main__.Producto object at 0x0000027915F7B740> ]

# * <__main__.Producto object at 0x0000027915F7B740>
print(verduleria1.lista_de_productos[2])
print(verduleria1.lista_de_productos[2].nombre)  # -> limón
# -> Buenas soy una fruta o una verdura
print(verduleria1.lista_de_productos[2].saludar())




class Productosss:
    def __init__(self) -> None:
        self.lista_de_productos = []

    def agregar_producto(self, nombre):
        producto = Producto(nombre)
        self.lista_de_productos.append(producto)

verduleria33 = Productosss()
verduleria33.agregar_producto("lechuga")
verduleria33.agregar_producto("naranja")
