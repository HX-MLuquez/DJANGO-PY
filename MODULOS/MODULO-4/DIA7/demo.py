

from abc import ABC, abstractmethod
import random


class Personaje(ABC):
    def __init__(self, hp: int, atk: int, df: int, arma: str = "") -> None:
        self.hp = hp
        self.atk = atk
        self.df = df
        self.arma = arma

    @abstractmethod
    def ataque(self) -> int:
        pass

    @abstractmethod
    def defensa(self, ataque: int) -> None:
        pass


class Jugador(Personaje):  # espada -> 3 + 2 = 5
    def ataque(self) -> int:
        return (self.atk + random.randint(1, 5) if self.arma else self.atk)

    def defensa(self, ataque: int) -> None:
        self.hp -= max(ataque - random.randint(1, self.df), 0)


class Monstruo(Personaje):
    def ataque(self) -> int:
        return self.atk + int(self.hp * 0.01)

    def defensa(self, ataque: int) -> None:
        self.hp -= max(ataque - (self.df + int(self.hp*0.001)), 0)


enfrentados = [Jugador(500, 10, 5, "espada"), Monstruo(1000, 1, 8)]
atk = 0

print(enfrentados[0].arma)

#           [False, False]
while any(e.hp <= 0 for e in enfrentados) == False:
    for e in enfrentados:
        if atk:
            e.defensa(atk)
        if e.hp > 0:
            atk = e.ataque() # 14
        else:
            print(f"¡Oh no!, el {e.__class__.__name__} ha muerto :(")
            break


# print(any([True, True])) # True  <- OR
# print(any([True, False])) # True
# print(any([False, False])) # False
