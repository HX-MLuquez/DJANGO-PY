from abc import ABC, abstractmethod


class SinGluten():
    tipo_producto = "Sin Gluten"


class Chocolate(ABC):
    def __init__(self, porc_cacao: float) -> None:
        self.porc_cacao = self.validar_porc_cacao(porc_cacao)

    @abstractmethod
    def validar_porc_cacao(self, porc: float) -> float:
        pass


class ChocolateAmargo(Chocolate):
    def validar_porc_cacao(self, porc: float):
        resultado = 0
        if 0.75 > porc:
            resultado = 0.75
        else:
            resultado = porc

        if 0.85 < resultado:
            resultado = 0.85
        else:
            resultado = resultado

        return min(max(0.75, porc), 0.85)
    #                 0.75


print(max((4-2), 0))
print(min((4-2), 1))


class ChocolateAmargoSinGluten(ChocolateAmargo, SinGluten):
    pass

choco1 = ChocolateAmargoSinGluten(1.5)

print(choco1.porc_cacao)
print(choco1.tipo_producto)
"""
0.85
Sin Gluten
"""