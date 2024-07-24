from abc import ABC, abstractmethod
from error import SubTipoInvalidoException
"""
De la clase Anuncio:
● Al crear, o al querer modificar el alto o el ancho de un anuncio ya creado, debe 
consultar si el valor que se quiere asignar es mayor a cero. De ser así, se asigna el 
valor ingresado. De no ser así, se asigna 1.
● Para esta etapa no se le solicita implementar las reglas de los atributos url_archivo
ni url_clic, pero sí debe definir sus getter y setter con la lógica básica de 
asignación de un nuevo valor al atributo correspondiente.
_ 2
www.desafiolatam.com 
● Al querer modificar el sub_tipo de algún anuncio ya creado, se debe validar que se 
esté ingresando un subtipo dentro de los permitidos en el tipo de la instancia actual. 
Los subtipos permitidos para las instancias de cada clase corresponden a los 
elementos de la tupla definida en el atributo de clase SUB_TIPOS respectivo. En caso 
de no cumplirse esta condición al momento de querer cambiar el valor del atributo 
sub_tipo, se debe lanzar una excepción SubTipoInvalidoException.
● El método mostrar_formatos es un método estático que muestra en pantalla los 
formatos y sus subtipos asociados disponibles para crear anuncios. Ejemplo:
FORMATO 1:
==========
- Subtipo 1
- Subtipo 2
Para ello debe referenciar los atributos de clase respectivos que contienen la 
información requerida (relación de colaboración señalada en el diagrama).
"""

"""
En otro archivo anuncio.py, definir la clase Anuncio y las clases que permitan 
crear instancias de tipo Video, Display y Social, cada una de ellas con sus 
atributos de clase y valores correspondientes respectivos.
"""


class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, value) -> None:
        self.__ancho = value if value > 0 else 1

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, value) -> None:
        self.__alto = value if value > 0 else 1

    @property
    def url_archivo(self) -> int:
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, value) -> None:
        self.__url_archivo = value

    @property
    def url_clic(self) -> int:
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, value) -> None:
        self.__url_clic = value

    @property
    def sub_tipo(self) -> int:
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, sub_tipo) -> None:
        if isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS:
            # completar   or   or
            raise SubTipoInvalidoException(
                "El sub tipo ... no existe en ese formato")
        else:
            self.__sub_tipo = sub_tipo

        # try:
        #     if sub_tipo in self.SUB_TIPOS:
        #         self.__sub_tipo=sub_tipo
        #     else:

    @staticmethod
    def mostrar_formatos() -> None:
        print()

    @abstractmethod
    def comprimir_anuncio(self) -> None:
        pass

    @abstractmethod
    def redimensionar_anuncio(self) -> None:
        pass


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion  # validar ¿??

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, value) -> None:
        pass

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, value) -> None:
        pass
    
    # ATRIBUTO cual GETTER SETTER duracion
    def comprimir_anuncio(self) -> None:
        print("")

 
    def redimensionar_anuncio(self) -> None:
         print("")




# Hacer las otras clases
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("", "")

    def comprimir_anuncio(self) -> None:
        print("")
    def redimensionar_anuncio(self) -> None:
         print("")
         
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("", "")

    def comprimir_anuncio(self) -> None:
        print("")
    def redimensionar_anuncio(self) -> None:
         print("")
         
# videito = Video("", "", "instream", 32)

# print(videito.sub_tipo) # -> instream

# videito.sub_tipo = "jujuju"
