

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False

    def devolver(self):
        if self.prestado:
            self.prestado = False
            return True
        return False

    def __str__(self) -> str:
        return f'titulo: {self.titulo}, autor: {self.autor}, prestado: {self.prestado}, isbn: {self.isbn}'


# libro1 = Libro("Relato de un náufrago", "Gabriel G. Márquez", 34511)
# print(libro1)
# # titulo: Relato de un náufrago, autor: Gabriel G. Márquez, prestado: False, isbn: 34511

# result_prestar1 = libro1.prestar()
# print(result_prestar1)
# print(libro1)

# result_prestar2 = libro1.prestar()
# print(result_prestar2)
# print(libro1)

# devolver1 = libro1.devolver()
# print(devolver1)
# print(libro1)


class Usuario:
    def __init__(self, nombre: str, id_usuario: int):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro: Libro):  # COLABORACION
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro: Libro):  # COLABORACION
        if libro.devolver():
            self.libros_prestados.remove(libro)
            return True
        return False


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro: Libro): # COLABORACION
        self.libros.append(libro)

    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.buscar_libro(isbn)
        if usuario and libro:
            return usuario.tomar_prestado(libro)
        return False

    def devolver_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.buscar_libro(isbn)
        if usuario and libro:
            return usuario.devolver_libro(libro)
        return False

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

libro1 = Libro("Relato de un náufrago", "Gabriel G. Márquez", 3451)
print(libro1) # prestado: False

libro2 = Libro("Relato de un náufrago", "Gabriel G. Márquez", 5345)
libro3 = Libro("El Quijote", "Cervantes", 2225)

user1 = Usuario("Manolo", 34)

biblioteca_ejemplo = Biblioteca() # {  libros->[ <l1 p=T> <l2> ]  usuarios->[ <34 [<l1 p=T>]> ]  }

biblioteca_ejemplo.agregar_libro(libro1)
biblioteca_ejemplo.agregar_libro(libro2)

biblioteca_ejemplo.registrar_usuario(user1)

biblioteca_ejemplo.prestar_libro(34, 3451)
biblioteca_ejemplo.devolver_libro(34, 3451) # {  libros->[ <l1 p=F> <l2> ]  usuarios->[ ]  }
# user1.tomar_prestado(libro1)
# print(libro1) # prestado: True

# user1.devolver_libro(libro1)
# print(libro1) # prestado: False
