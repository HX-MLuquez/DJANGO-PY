

from error import LargoExcedidoException
from anuncio import Video, Display, Social


class Campaña:
    def __init__(self, nombre, fecha_i, fecha_c, anuncios: list) -> None:
        self.__nombre = nombre
        self.__fecha_i = fecha_i
        self.__fecha_c = fecha_c
        self.__anuncios = [
            self.__obtener_instancias(a) for a in anuncios
        ]
        # for a in anuncios:
        #     if a["FORMATO"] == "Video":
        #         self.__anuncios.append(Video())

    def __obtener_instancias(self, anuncio: dict):
        tipo = anuncio.get("tipo", "")
        # if anuncio["sub_tipo"] in Video.SUB_TIPOS:
        if tipo == "Video":
            return Video(anuncio[""], anuncio[""], anuncio[""], anuncio["duracion"])
    # HACER demás IF
    
    @property 
    def nombre(self):
        # completar
        pass 
    
    @nombre.setter
    def nombre(self, nombre_nuevo):
        if len(nombre_nuevo) < 100:
            self.__nombre = nombre_nuevo 
        else:
            raise LargoExcedidoException("es demasiado extenso el .....")
    
    # Nombre de la campaña: Campaña 1
    # Anuncios: 1 Video, 2 Display, 0 Social
    def __str__(self) -> str:
        result = ["<Video>","<Video>","<Social>"]
        index_video = 0
        index_social = 0
        for a in result:
            print("completar")
        
        return f'Nombre de la campaña: {self.__nombre}\n '
        
    


# EJEMPLO SIMPLE

# class Anuncio:
#     def __init__(self, nombre, alto, ancho) -> None:
#         self.nombre = nombre
#         self.alto = alto
#         self.ancho = ancho


# mi_primer_anuncio = Anuncio("Tempo", 2, 3)
# print(mi_primer_anuncio.nombre)


# obj_dict_sasa = {
#     "nombre": "Fufu",
#     "alto": 2,
#     "ancho": 4
# }

# mi_primer_anuncio_desde_un_dict = Anuncio(obj_dict_sasa["nombre"], obj_dict_sasa["alto"], obj_dict_sasa["ancho"])
# print(mi_primer_anuncio_desde_un_dict.nombre)

# lista = [{
#     "nombre": "Fifi",
#     "alto": 2,
#     "ancho": 5
# }, {
#     "nombre": "Sese",
#     "alto": 1,
#     "ancho": 2
# }, {
#     "nombre": "Sisi",
#     "alto": 23,
#     "ancho": 1
# }]

# resultado= []
# for a in lista:
#     resultado.append(Anuncio(a["nombre"], a["alto"], a["ancho"]))

# print(resultado)

# print(resultado[0])

# print(resultado[0].nombre)

# class Campaña:
#     def __init__(self, anuncios: list) -> None: # [{}{}{}]
#         # self.anuncios = []
#         # for a in anuncios:
#         #     self.anuncios.append(Anuncio(a["nombre"], a["alto"], a["ancho"]))
#         # self.anuncios = [Video(a) for a in anuncios]
#         pass
