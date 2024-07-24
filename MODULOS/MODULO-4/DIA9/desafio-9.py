"""
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
        -__usuario: Usuario(nombre, apellido)
        -__respuestas: list
    }

"""