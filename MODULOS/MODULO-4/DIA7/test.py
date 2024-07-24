

class Persona:
    def __init__(self, edad) -> None:
        self.edad = edad
        
    def __eq__(self, otro):
        return self.edad == otro.edad 
    
per1 = Persona(12)
per2 = Persona(12)

print(per1 == per2) # True 

print(per1.edad == per2.edad)

edad = 14 

per3 = Persona(edad)

print("Hola")



