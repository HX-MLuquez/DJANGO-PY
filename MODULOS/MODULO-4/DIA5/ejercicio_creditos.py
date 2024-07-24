from abc import ABC, abstractmethod

# input ()
#  ● El tipo de crédito: las opciones son crédito de consumo, crédito comercial y crédito hipotecario
#  ● Monto del crédito
#  ● Correo de contacto del usuario solicitante


class SolicitudCredito(ABC):
    @abstractmethod
    def validar_monto(self, monto: str):
        pass

    @abstractmethod
    def validar_correo(self, correo: str):
        pass


class SolicitudCreditoDeConsumo(SolicitudCredito):
    __terminaciones = (".cl", ".com")

    def __init__(self, monto: int, correo: str):
        self.__monto = self.validar_monto(monto)
        self.__correo = self.validar_correo(correo)

    def validar_monto(self, monto: int):
        if monto < 1000000:
            monto = 1000000
        elif monto > 5000000:
            monto = 5000000
        return monto

    def validar_correo(self, correo: str):
        return (correo if correo.count("@") == 1 and correo.endswith(SolicitudCreditoDeConsumo.__terminaciones) else "")

    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, monto: int):
        self.__monto = self.validar_monto(monto)

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, correo: str):
        self.__correo = self.validar_correo(correo)


class SolicitudCreditoComercial(SolicitudCredito):

    __prohibidos = ("gmail", "outlook", "hotmail")
    __terminaciones = (".cl", ".com", ".org")

    def __init__(self, monto: int, correo: str):
        self.__monto = self.validar_monto(monto)
        self.__correo = self.validar_correo(correo)

    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, monto: int):
        self.__monto = self.validar_monto(monto)

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, correo: str):
        self.__correo = self.validar_correo(correo)

    def validar_monto(self, monto: int):
        if monto < 1000000:
            monto = 1000000
        elif monto > 5000000:
            monto = 5000000
        return monto

    def validar_correo(self, correo: str):
        return (correo if not any(p in correo.lower() for p in SolicitudCreditoComercial.__prohibidos) and correo.count("@") == 1 and correo.endswith(SolicitudCreditoComercial.__terminaciones) else "")


print("¡Gracias por solicitar un crédito con nuestro Banco!")
tipo = int(input("\nIngrese el Tipo de Crédito a solicitar:\n"
                 "1. Crédito de consumo\n"
                 "2. Crédito Comercial\n"
                 "3. Crédito Hipotecario\n"))
monto = int(input("\nIngrese el monto que desea solicitar:\n"))
correo = input("\nIngrese su correo de contacto:\n")

credito = None
if tipo == 1:
    credito = SolicitudCreditoDeConsumo(monto, correo)
elif tipo == 2:
    credito = SolicitudCreditoComercial(monto, correo)
# elif tipo == 3:
#     credito = SolicitudCreditoHipotecario(monto, correo)


