
"""
Tu amigo nuevamente ha solicitado tu ayuda, esta vez, para agregar tres pequeñas mejoras 
en el programa ya entregado. 
Mejora 1
Necesita que, en el caso de crear un mapper de Pokemon, se solicite además de la URL base 
el límite de registros a obtener al consultar por el listado completo, y almacenar este valor en 
un atributo de instancia. 
Mejora 2
Además, te comunica que su otro amigo (el que hizo la API), solicita que se aplique 
encapsulamiento de los atributos, tanto del que ya existía que contenía la URL base, como del 
nuevo solicitado que almacena el límite de registros (solo para pokemones).
Mejora 3
Finalmente, te solicita colocar un pequeño mensaje que aparezca en la terminal cada vez que 
se solicite el listado de personajes, indicando el listado que se está obteniendo
"""

import requests


class MonMapper:
    def __init__(self, base_url: str) -> None:
        self.__base_url = base_url
        
    @property 
    def base_url(self):
        return self.__base_url
    @base_url.setter 
    def base_url(self, value):
        self.__base_url = value
        
    def sumar(self):
        print("sese")

# ejemplo = MonMapper("https://")
# print(ejemplo.base_url)

# ejemplo.base_url = "wiwiwi"
# print(ejemplo.base_url)

# ejemplo.__base_url = 999

class PokemonMapper(MonMapper):
    def __init__(self, base_url: str, limit: int = 20) -> None:
        super().__init__(base_url) # 
        self.__limit = limit
        
    @property 
    def limit(self):
        return self.__limit
    @limit.setter 
    def limit(self, value):
        self.__limit = value
        
    def list_pokemon(self):
        print(f"El límite es: {self.__limit}")
        respuesta = requests.get(f'{self.base_url}?limit={self.__limit}')
        # print("----> ", respuesta) # <Response [200]>
        data = respuesta.json()
        print("--data--> ", data["results"]) 
        for poke in data["results"]:
            print(poke.get("name"))
        return data["results"]
    def poke_por_nombre(self, nombre):
         respuesta = requests.get(f'{self.base_url}/{nombre}')
         data = respuesta.json()
         print("Mi pokemon ", data["species"])
    
    def poke_por_nombre_en_lista_limitada(self, nombre):
        mis_pokemons = self.list_pokemon()
        pokemon = None 
        for poke in mis_pokemons:
            if poke["name"]== nombre:
                pokemon = poke 
        if pokemon is None:
            print("Poke no encontrado")
        else:
            print(":::", pokemon)
            
# https://pokeapi.co/api/v2/pokemon

poke_list_sample1 = PokemonMapper("https://pokeapi.co/api/v2/pokemon", 2)

poke_list_sample1.list_pokemon()

poke_list_sample1.poke_por_nombre("charmander")

poke_list_sample1.poke_por_nombre_en_lista_limitada("charmander")