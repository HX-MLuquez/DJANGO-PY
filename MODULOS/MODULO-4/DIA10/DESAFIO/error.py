
"""
* 1. En un archivo error.py, crear la excepción DimensionError derivada de Exception. 
Sobreescribir el constructor, recibiendo los parámetros mensaje, dimension y maximo, 
y asignándoles los respectivos atributos de instancia. 

* 2. En la misma clase anterior, sobrecargar el método __str__, de forma tal que si sólo 
se ha ingresado mensaje al crear la excepción, se retorna el método de la clase padre. 
En caso contrario, crear y retornar un mensaje de retorno utilizando los atributos 
mensaje y/o dimension y/o maximo.

"""


class Error(Exception):
    pass

class DimensionError(Error):
    def __init__(self, mensaje: str, dimension: int = None, maximo: int = None) -> None:
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
        
    def __str__(self) -> str:
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            res = self.mensaje
            
            if self.dimension: 
                res += f' La dimension es: {self.dimension}'
            if self.maximo: 
                res += f', El maximo es: {self.maximo}'
        return res 