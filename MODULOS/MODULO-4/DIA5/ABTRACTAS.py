
# ABSTRACTAS
from abc import ABC, abstractmethod

#* NO se INSTANCIA
#* DEBE DE TENER UN MÉTODO ABSTRACTO
#* ES SOLO UN MOLDE A TRANSFERIR A OTROS MOLDES (OTRAS SUB-CLASES)
#* LOS MÉTODOS ABSTRACTOS LOS DEBEMOS SOBRE-ESCRIBIR EN CADA UNA DE LAS SUB-CLASES

class Herramienta(ABC):
    def __init__(self, nombre, material) -> None:
        self.nombre = nombre 
        self.material = material
    @abstractmethod
    def calcular_fuerza(self):
        print("La fuerza inicial es de ...")

    def mostrar(self):
        print("Holis")
        return 101

# herramienta1 = Herramienta() #! TypeError: Can't instantiate abstract class Herramienta
# print(herramienta1.mostrar())

class Destornillador(Herramienta):
    def __init__(self, nombre, material, precio) -> None:
        super().__init__(nombre, material)
        self.precio = precio

    def mostrar(self):
        valor_de_lo_que_retorna_el_met_heredado = super().mostrar() # Extender mostrar()
        print("Bye")
    
    def calcular_fuerza(self):
        print("La fuerza inicial ya no es de ----- ...")
        super().calcular_fuerza() 
    def __str__(self) -> str:
        return f'{self.precio}'

destornillador1 = Destornillador("Philip", "Acero", 122)
destornillador1.mostrar()
print(destornillador1)