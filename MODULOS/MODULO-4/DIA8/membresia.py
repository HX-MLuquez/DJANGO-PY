

from abc import ABC, abstractmethod


class Membresia(ABC):
    def __init__(self, correo_electronico: str, numero_tarjeta: str) -> None:
        self.__correo_electronico = correo_electronico
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_electronico(self):
        return self.__correo_electronico

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_la_suscripcion(self, nueva_membresia: int):
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basica(self.correo_electronico, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_electronico, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_electronico, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_electronico, self.numero_tarjeta)


class Gratis(Membresia):
    costo = 0
    cantidad_dispositivos = 1

    def cambiar_la_suscripcion(self, nueva_membresia: int):
        # if nueva_membresia in [1,2,3,4]
        if nueva_membresia >= 1 and nueva_membresia <= 4:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

    def __str__(self) -> str:
        return f'''correo: {self.correo_electronico}
    N° Tarjeta: {self.numero_tarjeta}
    costo: {self.costo}'''


class Basica(Membresia):
    costo = 3000
    cantidad_dispositivos = 2

    def __init__(self, correo_electronico: str, numero_tarjeta: str) -> None:
        super().__init__(correo_electronico, numero_tarjeta)
        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.dias_de_regalo = 7
        if isinstance(self, Pro): #! solo pasar el elif a if y se soluciona el problema de que Pro accedía a 7 en vez de a 15...
            self.dias_de_regalo = 1556900

    def cambiar_la_suscripcion(self, nueva_membresia: int):
        # if nueva_membresia in [1,2,3,4]
        if nueva_membresia >= 2 and nueva_membresia <= 4:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

    def cancelar_subscripcion(self):
        return Gratis(self.correo_electronico, self.numero_tarjeta)


class Familiar(Basica):
    costo = 5000
    cantidad_dispositivos = 5

    def cambiar_la_suscripcion(self, nueva_membresia: int):
        # if nueva_membresia in [1,2,3,4]
        if nueva_membresia in [1, 3, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

    def control_parental(self):
        pass


class SinConexion(Basica):
    costo = 3500
    # cantidad_dispositivos = 2 # ya lo hereda

    def cambiar_la_suscripcion(self, nueva_membresia: int):
        # if nueva_membresia in [1,2,3,4]
        if nueva_membresia in [1, 2, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

    def cant_max_contenido_disponible(self):
        pass


class Pro(Familiar, SinConexion):
    costo = 7000
    cantidad_dispositivos = 6

    def cambiar_la_suscripcion(self, nueva_membresia: int):
        # if nueva_membresia in [1,2,3,4]
        if nueva_membresia in [1, 2, 3]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

    def control_parental(self):
        pass


gratis1 = Gratis("manolo@gmail.com", "4526-4334-0900-0002")
print(gratis1)

basica1 = gratis1.cambiar_la_suscripcion(1) # basica1 = Basica(gratis1.corre, gratis1.tarjeta)
print(basica1.costo)

familiar1 = basica1.cambiar_la_suscripcion(2) # familiar1 = Familiar(gratis1.corre, gratis1.tarjeta)
print(familiar1.costo)
print(familiar1.dias_de_regalo)

sinconexion1 = familiar1.cambiar_la_suscripcion(3) # sinconexion1 = SinConexion(gratis1.corre, gratis1.tarjeta)
print(sinconexion1.costo)

pro1 = sinconexion1.cambiar_la_suscripcion(4) # pro1 = Pro(gratis1.corre, gratis1.tarjeta)
print(pro1.costo)
print(pro1.dias_de_regalo)

cancelamos_grat1 = pro1.cancelar_subscripcion() # volvemos a gratis
print(cancelamos_grat1.costo)
print(cancelamos_grat1)

# grat33 = Gratis("mmm", "ojpo")
# print(grat33)

# bas1 = Basica("momo@gmail.com", "4321")
# print(bas1.correo_electronico)
# print(bas1.numero_tarjeta)

# Class Abstract - método -> cambiar_la_suscripcion ()-> nueva membresía

# OBJ -> Gratis, Básica, Familiar,
# Sin Conexión y Pro

# * Inst. (correo_electronico: str, numero_tarjeta: str)
# *  dias_de_regalo (alguna/s)  valor fijo

# * Gratis
# 1:Básica
# 2:Familiar
# 3:SinConexión
# 4:Pro

# def _crear_nueva_membresia(self, nueva_membresia: int):
#     if nueva_membresia == 1:
#         return Basico(self.correo_suscriptor, self.numero_tarjeta)
#     elif nueva_membresia == 2:
#         return Familiar(self.correo_suscriptor, self.numero_tarjeta)
#     elif nueva_membresia == 3:
#         return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
#     elif nueva_membresia == 4:
#         return Pro(self.correo_suscriptor, self.numero_tarjeta)


# class Familiar:
#     promo=121
#     def __init__(self, correo_electronico: str, numero_tarjeta: str) -> None:
#         self.__correo_electronico = correo_electronico
#         self.__numero_tarjeta = numero_tarjeta
#     def cambiar_la_suscripcion(self):
#        return Gratis(crear_nueva_membresia,numero_tarjeta)

# class Gratis:
#     def __init__(self, correo_electronico: str, numero_tarjeta: str) -> None:
#         self.__correo_electronico = correo_electronico
#         self.__numero_tarjeta = numero_tarjeta
#     def cambiar_la_suscripcion(self):
#        return Familiar(crear_nueva_membresia,numero_tarjeta)

# grat1 = Gratis("correo", "1223")

# fam3= grat1.cambiar_la_suscripcion()
