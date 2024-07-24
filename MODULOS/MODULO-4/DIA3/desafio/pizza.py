

class Pizza:

    precio = 10000
    tamanio = "familiar"

    proteicos = ["vacuno", "pollo", "carne vegetal"]
    vegetales = ["tomate", "aceitunas", "champiñones"]
    masas = ["tradicional", "delgada"]

    def __init__(self) -> None:
        self.proteico = ""
        self.vegetal1 = ""
        self.vegetal2 = ""
        self.tipo_masa = ""
        self.es_valido = False

    @staticmethod
    def validar(texto, lista):
        result = texto.lower() in lista  # True or False
        return result

    def solicitar(self):
        select_proteico = input(f"Ingrese una de estos ingredientes proteícos:\n - Vacuno\n - Pollo\n - Carne vegetal\n")
        self.proteico = select_proteico
        
        select_vegetal1 = input(f"Ingrese una de estos Vegetales:\n - Tomate\n - Aceitunas\n - Champiñones\n")
        self.vegetal1 = select_vegetal1
        
        select_vegetal2 = input(f"Ingrese otro de estos Vegetales:\n - Tomate\n - Aceitunas\n - Champiñones\n")
        if select_vegetal1 == select_vegetal2:
            print("Vegetal ya ingresado")
            
        self.vegetal2 = select_vegetal2
        select_masa = input(f"Ingrese el tipo de masa:\n - Tradicional\n - Delgada\n")
        self.tipo_masa = select_masa
        
        validar_proteina = self.validar(self.proteico, Pizza.proteicos) # Pollo <- True
        validar_vegetal1 = self.validar(self.vegetal1 , Pizza.vegetales) 
        validar_vegetal2 = self.validar(self.vegetal2 , Pizza.vegetales) 
        validar_masa = self.validar(self.tipo_masa , Pizza.masas) 
        
        self.es_valido = validar_proteina and validar_vegetal1 and validar_vegetal2 and validar_masa
        
        

"""
Dentro del mismo método del requerimiento 3, una vez asignados los valores a los 
atributos de la instancia, debe evaluarse si se trata de un ingreso válido (considerar la 
información de la descripción), usando el método del requerimiento 2. Si los 3 
ingredientes y el tipo de masa son válidos, deberá almacenar en un atributo el valor 
True. En caso contrario, deberá almacenar el valor False. Este atributo permitirá saber 
si una instancia específica es o no una Pizza válida. 
"""

"""
Para ello, dentro de la definición de este método, debe solicitar al 
usuario ingresar el ingrediente proteico, luego el primer ingrediente vegetal, luego el 
segundo ingrediente vegetal, y finalmente el tipo de masa. Cada ingreso debe 
almacenarse (o añadirse, si corresponde) en un atributo de la instancia.
"""

"""
En el mismo archivo y clase del requerimiento anterior, agregar un método que permita 
validar un elemento dentro de una lista de casos posibles. Este método se debe poder 
utilizar sin necesidad de crear un objeto de la clase, y debe recibir 2 argumentos: 
a. El elemento a validar (un texto). 
b. Los valores posibles a considerar para el elemento ingresado (una lista de 
textos). 
En caso de que el elemento ingresado como primer argumento se encuentre entre la 
lista de valores posibles ingresada como segundo argumento, el método debe retornar 
True. En caso contrario, debe retornar False. 

validar(texto, lista)
return Booleano
"""
