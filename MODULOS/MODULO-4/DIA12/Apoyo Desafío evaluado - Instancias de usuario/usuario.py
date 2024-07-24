class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.genero = genero
    def __str__(self) -> str:
        return f'nombre: {self.nombre} - apellido: {self.apellido}'

# usuario1 = Usuario("Toto", "Lopez", "www.gmail", "Male")

# print(usuario1)
        
