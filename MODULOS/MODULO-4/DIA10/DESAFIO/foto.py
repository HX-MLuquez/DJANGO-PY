
"""

* 3. En el archivo foto.py entregado, modificar los métodos setter de alto y ancho, de forma 
tal que se lance una excepción de tipo DimensionError en caso de que el nuevo valor 
ingresado no cumpla con las condiciones descritas. En caso contrario, asignar el 
nuevo valor al atributo de instancia correspondiente.

"""
from error import DimensionError

# min 1


class Foto:
    MAX = 2000

    def __init__(self, ancho: int, alto: int, link: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.link = link

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        if ancho > Foto.MAX:
            raise DimensionError(
                "El ancho se pasa el límite máximo", ancho, Foto.MAX)
        elif ancho < 1:
            raise DimensionError("El ancho se pasa el límite mínimo", ancho)
        else:
            self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto):
        try:
            if alto > Foto.MAX:
                raise DimensionError(
                    "El alto se pasa el límite máximo", alto, Foto.MAX)
            elif alto < 1:
                raise DimensionError("El alto se pasa el límite mínimo", alto)
            else:
                self.__alto = alto
                print(f'El alto se a actualizado correctamente a {self.__alto}')
        except DimensionError as e:
            print(f'Nuetra exception es --> {e}')


foto1 = Foto(400, 400, "baba.jpg")
print(foto1.ancho)



foto_error = Foto(3000, 1000, "data.png")
foto_error.alto = 9000

