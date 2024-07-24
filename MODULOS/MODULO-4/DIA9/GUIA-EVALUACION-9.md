




# Diagrama de Clases

```plaintext
--------------------------
|     Alternativa        |
--------------------------
| + contenido: str       |
| + ayuda: str           |
--------------------------
| + mostrar_alternativa()|                
--------------------------

            ▲
            |
            |
-------------------------
|      Pregunta         |
-------------------------
| + enunciado: str      |
| + ayuda: str          |
| - alternativas: list  | Lista con dict  List[dict]
| + requerido: bool     |
-------------------------
| + mostrar_pregunta()  |
-------------------------

            ▲
            |
            |
---------------------------------
|       Encuesta                |
---------------------------------
| + nombre: str                 |
| - preguntas: List[dict]       | self.__preguntas = [Pregunta(p["enunciado"],p["ayuda"],
|                               |                       p["alternativas"],p["requerido"]) for p in preguntas]
| - listados_respuestas: list   |
---------------------------------
| + mostrar_encuesta()          |
| + agregar_listado_respuestas  |
|    (listado_respuestas: list) |
---------------------------------
         ▲                      ▲
        /                        \
       /                          \
      /                            \
     v                              v
---------------------------    -----------------------------------
| EncuestaLimitadaEdad    |    | EncuestaLimitadaRegion          |
---------------------------    -----------------------------------
| - edad_min: int         |    | - regiones: list[int]           |
| - edad_max: int         |    -----------------------------------
---------------------------    |            GETTERS              |
|          GETTERS        |    |           SETTER/S              |
|          SETTER/S       |    |                                 |
|                         |    -----------------------------------
| + agregar_respuesta     |    | + agregar_respuesta(respuestas: |
|(respuestas:             |    |              ListadoRespuestas) |
|      ListadoRespuestas) |    -----------------------------------
---------------------------   
                            

            ▲  * Encuesta  EncuestaLimitadaEdad  EncuestaLimitadaRegion  ListadoRespuestas
            |
            |
----------------------------
|       Usuario            |
----------------------------
| - correo: str            |
| - edad: int              |
| - region: int            |
----------------------------
|           GETTERS        |
|           SETTER/S       |                 
| + contestar_encuesta     |
|(encuesta: Union[Encuesta,|
|EncuestaLimitadaEdad,     |
|EncuestaLimitadaRegion],  |
|respuestas: list)         |
----------------------------

            ▲
            |
            |
---------------------------
| ListadoRespuestas       |
---------------------------
| - usuario: Usuario      |
| - respuestas: list      |
---------------------------
|        GETTERS          |
---------------------------
```

**Utilizado, Contesta, Utiliza o Contiene son maneras de informar como colaboran (agregación) las clases**

```mermaid
classDiagram
    Pregunta --> Contiene --> Alternativa

    Encuesta --> Contiene --> Pregunta 

    EncuestaLimitadaEdad --> Contiene -->  Pregunta (por herencia) 
    EncuestaLimitadaEdad --> Contiene --> ListadoRespuestas

    EncuestaLimitadaRegion --> Contiene -->  Pregunta (por herencia) 
    EncuestaLimitadaRegion --> Contiene --> ListadoRespuestas

    Usuario --> Contiene --> Encuesta 
    Usuario --> Contiene --> EncuestaLimitadaEdad
    Usuario --> Contiene --> EncuestaLimitadaRegion
    Usuario --> Contiene --> ListadoRespuestas

    ListadoRespuestas --> Contiene --> Usuario

    
    class Alternativa {
        +contenido: str
        +ayuda: str
        -----------------------
        +mostrar_alternativa()
    }

    class Pregunta {
        +enunciado: str
        +ayuda: str
        -__alternativas: list
        +requerido: bool
        -----------------------
        +mostrar_pregunta()
    }

    class Encuesta {
        +nombre: str
        -__preguntas: List[dict]
        -__listados_respuestas: list
        -----------------------
        +mostrar_encuesta()
        +agregar_listado_respuestas(listado_respuestas)
    }

    class EncuestaLimitadaEdad {
        -__edad_min: int
        -__edad_max: int
        -----------------------
        +agregar_respuesta(respuestas: ListadoRespuestas)
    }

    class EncuestaLimitadaRegion {
        -__regiones: List[int]
        -----------------------
        +agregar_respuesta(respuestas: ListadoRespuestas)
    }

    class Usuario {
        -__correo: str
        -__edad: int
        -__region: int
        List[int]
        +contestar_encuesta(encuesta: Union[Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion], respuestas: list)
    }

    class ListadoRespuestas {
        -__usuario: Usuario
        -__respuestas: list
    }

```

```
```

# EXTRA
## EJEMPLOS AGREGACIONES - COLABORACIONES

```python
class Motor:
    def encender(self):
        print("El motor está encendido")

class Coche:
    def __init__(self, motor: Motor): 
        self.motor = motor
    
    def arrancar(self):
        self.motor.encender()
        print("El coche está en marcha")

# Uso
motor = Motor()
coche = Coche(motor)
coche.arrancar()
```

```python
class Libro:
    def __init__(self, titulo: str):
        self.titulo = titulo

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
    
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.titulo)

# Uso
libro1 = Libro("El Principito")
libro2 = Libro("1984")
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.mostrar_libros()
```

```python
class Calculadora:
    def sumar(self, a: int, b: int) -> int:
        return a + b

class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def usar_calculadora(self, calc: Calculadora, a: int, b: int):
        resultado = calc.sumar(a, b)
        print(f"{self.nombre} obtuvo el resultado: {resultado}")

# Uso
calculadora = Calculadora()
usuario = Usuario("Juan")
usuario.usar_calculadora(calculadora, 5, 3)
```

```python
class Pregunta:
    def __init__(self, texto: str):
        self.texto = texto

class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def contestar_pregunta(self, pregunta: Pregunta, respuesta: str):
        print(f"{self.nombre} respondió '{respuesta}' a la pregunta: {pregunta.texto}")

# Uso
pregunta = Pregunta("¿Cuál es tu color favorito?")
usuario = Usuario("Ana")
usuario.contestar_pregunta(pregunta, "Azul")
```