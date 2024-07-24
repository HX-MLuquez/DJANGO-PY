
# publicos _protegidos __privados  @property GETTER   @nombre.setter SETTER (Mutar - Validar)
#         _protegidos -> modificar desde la Clase o desde las sub-clases
#         __privados -> modificar desde la Clase solamente


class Personaje: 
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        
    @property 
    def nombre(self):  # nombre <-> _nombre
        return f'Nombre es: {self.__nombre}'
    @nombre.setter 
    def nombre(self, value):
        if type(value) != str:
            print("Debe ser un string")
        elif len(value) < 3:
            print("Debe tener 3 caracteres o mas")
        elif value == self.__nombre:
            print("Es el mismo nombre")
        else:
            self._nombre = value 
            print(f"El nuevo nombre es {self.__nombre}")
        

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

# mago.__nombre ->  _Personaje__nombre
 

print(mago.nombre)

print("--------------------------")
print(mago._Personaje__nombre)

mago._Personaje__nombre = 5040

print(mago._Personaje__nombre)


#------------------------------------------------------------------
print("\n----------- EJEMPLO con _guion (privada por convención) ---------------\n")

class Persona:
    _humano = True
    def __init__(self, nombre, edad=18) -> None:
        self._nombre = nombre 
        self.edad = edad
    @property 
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        print("Dentro del SETTER")
        if type(value) != str:
            print("Debe ser un string")
        else:
            self._nombre = value
            print(f"Se ha cambiado el nombre por: {self._nombre}")
        
persona1 = Persona("Jim")
# persona1._nombre = 2332 #! NO lo hagas por favor
print(persona1.nombre)

persona1.nombre = "Neo"
print(persona1.nombre)


#------------------------------------------------------------------
print("\n----------- EJEMPLO con __dobleGuion (privada por convención) ---------------\n")

class Producto:
    def __init__(self, nombre, stock) -> None:
        self.nombre = nombre
        self.__stock = stock 
    @property 
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, value):
        print("Dentro del SETTER")
        if type(value) != int:
            print("Debe ser un número")
        else:
            self.__stock = value
            print(f"Se ha cambiado el stock a: {self.__stock}")    
            
producto1 = Producto("Tv", 4)

# print(producto1.__stock) #! AttributeError: 'Producto' object has no attribute '__stock'

#* __stock  -->   _Producto__stock
# print(producto1._Producto__stock) #! Por favor no hagan esto

producto1.stock = 34
print(producto1.stock)