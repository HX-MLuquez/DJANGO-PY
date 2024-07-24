
class Pelota:
    posiciones = [3, 5, 2]
    
    def saludar():
        mensaje="Hola"
        return mensaje

    @staticmethod
    def crear_rebote():
        posiciones = [3, 0, 5, 0, 2, 0, 1, 0, 0, 0]
        return posiciones

    @staticmethod
    def imprimir_pos():
        Pelota.crear_rebote() # Ejecuto un método dentro de otro método
        print(Pelota.posiciones)

print(Pelota.crear_rebote()) # -> [3, 0, 5, 0, 2, 0, 1, 0, 0, 0]

Pelota.imprimir_pos() # -> [3, 5, 2]

#!IMPORTANTE
#* ATRIBUTOS ESTÁTICOS    CLASE.ATRIBUTO
#* ATRIBUTOS de INSTANCIA   SELF.ATRIBUTO