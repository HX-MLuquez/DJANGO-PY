

#todo: __eq__

class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def __eq__(self, otro):
        return self.nombre == otro.nombre # BOOLEAN

persona1 = Persona("Manolo") 
persona2 = Persona("Juan Carlos")
persona3 = Persona("Manolo") 

print(persona1.nombre)
print(persona2.nombre)

print(persona1 == persona2) # False

print(persona1 == persona3) # True