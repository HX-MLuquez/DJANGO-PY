
#* 3 maneras de dar VALOR a los atributos del Constructor

class Persona:
    peso = 98
    #* CONSTRUCTOR - ATRIBUTOS de INSTANCIA
    def __init__(self, nombre, edad = 18) -> None:
        self.nombre = nombre
        self.active = False
        self.edad = edad
        self.pais = "Perú"
    
    def __str__(self) -> str:
        return f'nombre: {self.nombre}, edad: {self.edad}'
        

print(Persona.peso)

#* INSTANCIA

persona1 = Persona("Manolo")

print(persona1) # -> nombre: Manolo, edad: 18  <- <__main__.Persona object at 0x000001B0C424A8A0>


        

        
