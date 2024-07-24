

from typing import Union, List


class Foto:
    def __init__(self, imagen: str, ancho: int, alto: int) -> None:
        self.__imagen = imagen
        self.__ancho = ancho
        self.__alto = alto
        self.__reacciones = 0

    @property
    def imagen(self) -> str:
        return self.__imagen

    @imagen.setter
    def imagen(self, imagen: str) -> None:
        self.__imagen = imagen

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        self.__alto = alto

    @property
    def reacciones(self) -> int:
        return self.__reacciones

    @reacciones.setter
    def reacciones(self, reacciones: int) -> None:
        self.__reacciones = reacciones


class FotoPerfil(Foto):
    def __init__(self) -> None:
        super().__init__(
            "extras/user.png",
            400,
            400
        )
        self.__recorte = [
            (0, 0),
            (self.ancho, 0),
            (0, self.alto),
            (self.ancho, self.alto)
        ]


class Usuario():
    def __init__(self, correo: str, contraseña: str) -> None:
        self.__correo = correo
        self.__contraseña = contraseña
        self.__album_fotos = []
        self.__foto_perfil = FotoPerfil()

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, correo: str) -> None:
        self.__correo = correo

    @property
    def contraseña(self) -> str:
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, contraseña: str) -> None:
        self.__contraseña = contraseña

    @property
    def album_fotos(self) -> List[Foto]:
        return self.__album_fotos

    def agregar_fotos_al_album(self, imagen: str, ancho: int, alto: int) -> None:
        self.__album_fotos.append(Foto(imagen, ancho, alto))

    @property
    def foto_perfil(self) -> Foto:
        return self.__foto_perfil

    def actualizar_foto_perfil(self, imagen: str, ancho: int, alto: int) -> None:
        self.__foto_perfil.imagen = imagen
        self.__foto_perfil.ancho = ancho
        self.__foto_perfil.alto = alto

    def reaccionar(self, foto: Union[Foto, FotoPerfil]) -> None:
        foto.reacciones += 1


usuario1 = Usuario("mau@gmail.com", "1234")

print(usuario1.foto_perfil)

foto1 = Foto("img.png", 320, 500)

usuario1.agregar_fotos_al_album("img.png", 320, 500)
usuario1.agregar_fotos_al_album("img2.png", 3200, 5040)

print(usuario1.album_fotos[0].imagen) # "img.png"
print(usuario1.album_fotos[1].imagen) # "img.png"