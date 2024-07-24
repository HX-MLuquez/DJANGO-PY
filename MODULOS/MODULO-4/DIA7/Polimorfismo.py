
from abc import ABC, abstractmethod

class Pelota(ABC):
    @abstractmethod
    def rebotar(self, altura:int):
        pass



class PelotaPlastico(Pelota):
    def rebotar(self, altura:int):
        rebote = 3
        resultado = rebote * altura 
        print(resultado)
        return resultado
        
class PelotaAcero(PelotaPlastico):
    def rebotar(self, altura:int):
        data_met_padre = super().rebotar(altura) # 24
        rebote = 1
        resultado = (rebote * altura) - data_met_padre
        print(resultado)

plastico1 = PelotaPlastico()
plastico1.rebotar(8)

acero1 = PelotaAcero()
acero1.rebotar(8)
