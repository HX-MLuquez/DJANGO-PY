

class Persona:
    def __init__(self, nombre, edad, email) -> None:
        self.nombre = nombre
        self.edad = edad
        self._email = email # _email <- Atributo Privado
    def __str__(self) -> str:
        return f'nombre: {self.nombre}, email: {self._email}'
    
persona2 = Persona("Jimy", 22, "jim@gmail.com")

print(persona2) # nombre: Jimy, email: jim@gmail.com
persona2._email = "nada"

print(persona2)