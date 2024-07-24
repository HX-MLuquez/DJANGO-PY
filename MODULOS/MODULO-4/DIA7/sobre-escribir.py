

class PelotaDeporte:
    def __init__(self, color) -> None:
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


p1 = PelotaDeporte("Azul")
p1.color = "roja"


class PelotaHija(PelotaDeporte):
    def __init__(self) -> None:
        self.__color = "violeta"

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        pass


p2 = PelotaHija()
p2.color = "rojo"

print(p2.color)
