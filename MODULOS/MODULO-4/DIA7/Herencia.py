

class Pelota:
    tipo = "algo"

    def __init__(self, color) -> None:
        self.color = color


class PelotaHija(Pelota):
    # def __init__(self, color) -> None:
    #     super().__init__(color)
    def mostrar_color(self):
        print(f'El color de la pelota es: {self.color}')


pelo1 = PelotaHija("Amarillo")
pelo1.mostrar_color()

print("----------------------------------------------------")


class Abuelo:
    tipo = "descansa"

    def __init__(self) -> None:
        self.quien = "soy el abuelo"

    def saluda(self):
        print("holllaaa")


class Papa(Abuelo):
    tipo = "corre"

    def __init__(self) -> None:
        self.quien = "yo soy el padre"
        self.veo = "el futuro"
        super().__init__()

    def estornuda(self):
        print("aaaaaaaaa chissss")

# primer_papa = Papa()
# print(primer_papa.tipo)
# print(primer_papa.quien)
# primer_papa.saluda()


class Hijo(Papa):
    def __init__(self) -> None:
        self.edad = 10
        super().__init__()


hijo1 = Hijo()
hijo1.saluda()
hijo1.estornuda()


print("----------------------------------------------------")


class PelotaDeportePadre:
    tipo = "deporte"

    def __init__(self) -> None:
        self.velocidad = 33

    def sonido(self):
        print("toc")


class PelotaPlasticoMadre:
    # tipo = "plastico"
    def __init__(self) -> None:
        self.soy = "pelota de plastico"
        self.velocidad = 500

    def sonido(self):
        print("tin tin tin")

    def soyMama(self):
        print("soy la madre")


class PelotaHijaDePingPong(PelotaPlasticoMadre, PelotaDeportePadre):
    def __init__(self) -> None:
        self.suena = "weweeee"
        super().__init__()


print(PelotaHijaDePingPong.tipo)

pelota1 = PelotaHijaDePingPong()
print(pelota1.tipo)
print(pelota1.sonido())  # toc
print(pelota1.velocidad)  # 33
# print(pelota1.soy) #! ATTR del constructor de la clase Padre que no está a su izquierda
print(pelota1.soyMama())  # soy la madre


##################################################

# nombre, id >
class Catalogo:
    def __init__(self) -> None:
        self.lista = []


class Producto:
    # nombre, precio, descripción, id, stock
    pass

class Pc(Producto):
    # partes
    pass

class Tv(Producto):
    # pulgada
    pass

# {nombre, precio, descripción, id, stock}


class Productos:
    def __init__(self) -> None:
        self.lista_productos = []
    # AGREGACIÓN NORMAL - COLABORACIÓN - INDEPENDIENTE  
    def agregar_productos(self, producto: Producto):
        self.lista_productos.append(producto)
    
     # AGREGACIÓN FUERTE - COMPOSICIÓN - DEPENDIENTE   
    def agregar_productos_2(self, producto: dict):
        self.lista_productos.append(Producto(producto["nombre"], producto["precio"], producto["descripcion"]))
        

prod1 = Producto(...)

mi_lista_productos = Productos(...) 

mi_lista_productos.agregar_productos(prod1)
