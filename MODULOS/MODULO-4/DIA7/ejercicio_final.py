from abc import ABC, abstractmethod
import random


class NPC():
    def __init__(self, nombre: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__nombre = nombre

    def mostrar_dialogo(self, mensaje: str) -> None:
        print(f"{self.__nombre}: {mensaje}")


class Personaje(ABC):
    def __init__(self, hp: int, atk: int, df: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__hp = hp
        self.__atk = atk
        self.__df = df

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, hp) -> None:
        self.__hp = hp

    @property
    def atk(self) -> int:
        return self.__atk

    @property
    def df(self) -> int:
        return self.__df

    @abstractmethod
    def ataque(self) -> None:
        pass

    @abstractmethod
    def defensa(self, ataque: int) -> None:
        pass


class Jugador(Personaje):
    def __init__(self, hp: int, atk: int, df: int, arma: str = None) -> None:
        super().__init__(hp, atk, df)
        self.__arma = arma

    def ataque(self) -> int:
        return (self.atk + random.randint(1, 5) if self.arma else self.atk)

    def defensa(self, ataque: int) -> None:
        self.hp -= max(ataque - random.randint(1, self.df), 0)


class Monstruo(Personaje, NPC):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def ataque(self) -> int:
        return self.atk + int(self.hp * 0.01)

    def defensa(self, ataque: int) -> None:
        self.hp -= max(ataque - (self.df + int(self.hp*0.001)), 0)


mounstrito = Monstruo(hp=1000, atk=1, df=8, nombre="Bégimo")
mounstrito.mostrar_dialogo("GRAAAWR")
jugador = Jugador(500, 10, 5, "espada")

#                 0          1
enfrentados = [jugador, mounstrito]
atk = 0

while any(e.hp <= 0 for e in enfrentados) == False:
    for e in enfrentados:
        if atk:
            e.defensa(atk)
        if e.hp > 0:
            atk = e.ataque()
        else:
            if isinstance(e, Monstruo):
                print("¡Felicidades!, ¡Haz ganado la batalla")
            elif isinstance(e, Jugador):
                print("¡Oh no!, haz perdido la batalla :(")
            break
