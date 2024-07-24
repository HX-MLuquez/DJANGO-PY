
# DetalleVentaItem
class Producto():
    def __init__(self, producto: str, cantidad: int):
        self.__producto = producto
        self.__cantidad = cantidad

    @property
    def producto(self):
        return self.__producto

    @property
    def cantidad(self):
        return self.__cantidad

# DetalleVenta


class DetalleProductosVenta():
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto: Producto): # COLABORACIÓN
        self.__productos.append(producto)

    def __str__(self):
        retorno = (":::::::: DETALLE DE ESTA VENTA :::::::::\n"
                   "PRODUCTO\tCANTIDAD\n")
        productos = []
        for p in self.__productos:
            # -> ["tv  4", "celu  2"]
            productos.append(f'{p.producto}  {p.cantidad}\n')

        return f"{retorno}{''.join(productos)}"


class Venta():
    def __init__(self):
        self.__detalle = DetalleProductosVenta() # COMPOSICION - AGREGACION FUERTE
        # ->  OBJE -> ATR. [ ]   MET agregar_producto()
    def crear_producto_insertar_en_lista(self, producto: str, cantidad: int):
        detalle_venta_producto = Producto(producto, cantidad) # COMPOSICION - AGREGACION FUERTE
        self.__detalle.agregar_producto(detalle_venta_producto)
    @property
    def detalle(self):
       return self.__detalle


print("Hola bienvenidos a la planilla para sdñljfasodfkáposkdfpak")

print("quieres cargar una venta")
res = int(input("1 si 2 no"))
venta_original = Venta()
while res == 1:
    nombre= input("Nombre del prod.....")
    cant= input("cant del prod.....")
    
    venta_original.crear_producto_insertar_en_lista(nombre,cant)
    
    print(venta_original.detalle)
    
    res = int(input("1 si 2 no"))
print("chau")




venta1 = Venta()
venta1.crear_producto_insertar_en_lista("tv", 4)
venta1.crear_producto_insertar_en_lista("celu", 2)
print(venta1.detalle)
"""
:::::::: DETALLE DE ESTA VENTA :::::::::
PRODUCTO        CANTIDAD
tv  4
celu  2
"""
# producto1 = Producto("tv", 4)
# print(producto1.producto)

# lista_de_productos = DetalleProductosVenta()  # -> [ <producto1> ]

# lista_de_productos.agregar_producto(producto1)

# print(lista_de_productos)
