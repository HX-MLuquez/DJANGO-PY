
#* GETTER  (VER) -> @property
#* SETTER  (MODIFICAR - MUTADORES) -> @metodo.setter

class Persona:
    def __init__(self, nombre) -> None:
        self._nombre = nombre
    
    @property # Decorador property <- VER <- GETTER
    def nombre(self): #* <- enlace directo a este Atributo self._nombre
        return self._nombre
    
    @nombre.setter #* Decorador mismo nombre_del_getter.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre == "Cacho":
            print("Ese nombre no se debe utilizar")
        else:
            self._nombre = nuevo_nombre
    
persona3 = Persona("Jose")

print(persona3.nombre) # -> Jose
print(persona3._nombre) # -> Jose

persona3.nombre = "Cacho" # Ese nombre no se debe utilizar
print(persona3.nombre)

persona3._nombre = "Cacho"

print(persona3.nombre)