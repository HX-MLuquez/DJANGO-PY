"""
Constructor (considera parámetros y valores asignados 
 a. atributos de instancia)
 b. Getter de estado.
 c. Setter de estado.
 d. Sobrecarga para comparar “menor que” .
 e. Sobrecarga para comparar “mayor que”.
 f. Sobrecarga para comparar “igual que” (opcional).
 g. Método de instancia que retorna la probabilidad de la instancia actual de
 ganar respecto de otra instancia (opcional).
 h. Método que muestra diálogo de enfrentamiento al orco (incluyendo
 probabilidad de ganar) y retorna opción escogida por el jugador (opcional).
"""


class Personaje:

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self):
        return f'Nombre: {self.nombre}, Nivel: {self.nivel}, Experiencia: {self.experiencia} '

    @estado.setter
    def estado(self, value):  # mago.estado = 50   -30
        res_exp = self.experiencia + value
        if res_exp >= 100:
            self.nivel += 1
            res_exp -= 100
        if res_exp < 0:
            if self.nivel == 1:
                res_exp = 0
            else:
                self.nivel -= 1
                res_exp = 100 - res_exp
        self.experiencia = res_exp

    def __eq__(self, otra):
        return self.nivel == otra.nivel

    def __lt__(self, otra):
        return self.nivel < otra.nivel

    def __gt__(self, otra):
        return self.nivel > otra.nivel

    def get_probabilidad_de_ganar(self, otra):
        if self < otra:
            return 0.33
        elif self > otra:
            return 0.66
        else:
            return 0.5
    #  Puedes agregar en la clase un método estático que reciba por parámetro la probabilidad, muestre en pantalla todo lo requerido y retorne la opción de juego del usuario.

    @staticmethod
    def mostrar_dialogo(probabilidad_ganar):
        return int(input(
            f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
            "de probabilidades de ganarle al Orco.\n"
            "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \n"
            "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n"
            "\n¿Qué deseas hacer?\n"
            "1. Atacar\n"
            "2. Huir\n"
        ))


if __name__ == "__main__": #! Cuidado con la sintaxis incorrecta como _main__ o lo que sea incorrecto ya que al ser un condicional no correrá nada
    opcion = Personaje.mostrar_dialogo(0.5)  # 1

    mago = Personaje("Neo")
    print(mago.estado)

    orco = Personaje("Orco")

    print(orco.estado)

    print(orco == mago)  # True

    mago.get_probabilidad_de_ganar(orco)

