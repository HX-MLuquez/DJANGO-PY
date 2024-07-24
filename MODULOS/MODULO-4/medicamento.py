# archivo medicamento.py
class Medicamento:

    def __init__(self) -> None:
        self.precio = None
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0 # True
    
    def asigna_precio(self, precio_entregado: int):
        es_valido = self.validar_mayor_a_cero(precio_entregado)
        if es_valido:
            self.precio = precio_entregado
            print(f'Agregamos a precio el valor {self.precio}')
        else:
            print(f"El precio '{precio_entregado}' no es un precio válido")

#* creamos INSTANCIA y que obtenemos el OBJETO medicamento_nuevo           
medicamento_nuevo = Medicamento()

medicamento_nuevo.asigna_precio(0)
# asigna_precio(5)
# es_valido = validar_mayor_a_cero(5) -> True

"""
OBJETO
medicamento_nuevo = {
    precio: None,                Atributos
    ----------------------------------------
    validar_mayor_a_cero: def     Métodos
    asigna_precio: def
}

"""
