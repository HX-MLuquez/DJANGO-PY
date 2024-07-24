
# _privado publico  @property GETTER   @nombre.setter SETTER (Mutar - Validar)


class Personaje: 
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        
    @property 
    def nombre(self):  # nombre <-> _nombre
        return f'Nombre es: {self._nombre}'
    @nombre.setter 
    def nombre(self, value):
        if type(value) != str:
            print("Debe ser un string")
        elif len(value) < 3:
            print("Debe tener 3 caracteres o mas")
        elif value == self._nombre:
            print("Es el mismo nombre")
        else:
            self._nombre = value 
            print(f"El nuevo nombre es {self._nombre}")
        

mago = Personaje("Neo")

# print(mago._nombre) #! No me deja
print(mago.nombre) # VER
mago.nombre = 101 # me deja mutar 

print(mago.nombre)

mago.nombre = "Qu" # me deja mutar 

print(mago.nombre)

# SETTER    ->  mago.nombre = "Neo"  mago.nombre("Neo")
mago.nombre = "Neo" # me deja mutar 

print(mago.nombre)

mago._nombre = 92344590287 

print(mago.nombre)