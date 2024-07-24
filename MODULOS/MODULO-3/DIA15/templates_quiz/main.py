
# No modificar
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import time
import os
import sys

# valores iniciales -
n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10  # 0, 1, 3
op_sys = 'cls' if sys.platform == 'win32' else 'clear'


# ----------------------------------------

os.system(op_sys)  # limpiar pantalla

print('Bienvenido a la Trivia')  # -> "1"
opcion = input('''Ingrese una opción para Jugar! 
        1. Jugar
        0. Salir
        
    > ''')

"""
validate(opciones, eleccion)
Args:
    opciones: [LIST] Ejemplo ["0", "1"]
    eleccion: STRING
Return:
    Manejo Error - input("Ingrese opción válida")
    eleccion
"""
# todo: 1. validar opcion / #* opcion es igual a opcion en caso de sea opción válida
opcion = validate(["0", "1"], opcion)  # -> return "1"

# todo: 2. Definir el comportamiento de Salir
if opcion == '0':
    print("Nos vemos pronto!!!")  # * Ver que mensaje Mostrar
    time.sleep(2)
    os.system(op_sys)
    exit()
    # finalizar programa
    #! IMPORTANTE manejar corte de programa

# Funcionamiento de preguntas
while correcto and n_pregunta < 3*p_level:

    if n_pregunta == 0:
        p_level = input(
            '¿Cuántas preguntas por nivel? (Máximo 3) [1-3]: ')  # -> "2"

        """
        validate(opciones, eleccion)
        Args:
            opciones: [LIST] Ejemplo ["0", "1"]
            eleccion: STRING
        Return:
            Manejo Error - input("Ingrese opción válida")
            eleccion
        """
        # todo: 3. Validar el número de preguntas por nivel / #* Aplicar el int(validate(opciones, eleccion)) a razón de que lo ya validado pase a número por la necesidad de luego trabajar con este
        p_level = int(validate(["1", "2", "3"], p_level))  # -> "2" <- int 2

    if continuar == 'y':
        # contador de preguntas
        n_pregunta += 1  # *   0 -> 1

        """
                   *   0-> 1     ,   2
        choose_level(n_pregunta, p_level)
        Args:
            n_pregunta: Number  
            p_level: Number  # * nuestra selección entre 1 y 3
        Return:
            level: String - 'basicas'
            * Ejemplo:  Dado que seleccionamos p_level -> 2      n_pregunta <= p_level   |  n_pregunta <= 2*p_level 
                    *   n_pregunta 1 -> 'basicas'   n_pregunta 2 -> 'basicas'
                    *   n_pregunta 3 -> 'intermedias'   n_pregunta 4 -> 'intermedias'
                    *   n_pregunta 5 -> 'avanzadas'   n_pregunta 6 -> 'avanzadas'
        """
        # todo: 4. Escoger el nivel de la pregunta /#*  choose_level(n_pregunta, p_level)
        nivel = choose_level(n_pregunta, p_level)

        print(f'Pregunta {n_pregunta}:')
        # print(f'Nivel es: {nivel}')

        """
        choose_q(nivel)
        Args:
            nivel: String (Ejemplo: 'basicas')  
        Return:
            Tupla: (enunciado, alternativas)
            *enunciado -> Lista con único enunciado
            *alternativas -> Lista
        """
        # todo: 5. Escoger el enunciado y las alternativas de una pregunta según el nivel escogido
        enunciado, alternativas = choose_q(nivel)  # -> 'basicas'
        # print(enunciado, alternativas)

        """
        print_pregunta(enunciado, alternativas)
        Args:
            enunciado: Lista con único enunciado dentro (Ejemplo: ['Vamos que se puede'])  
            alternativas: Lista
        Return:
            None   /  (solo imprime)
        """
        # todo: 6. Imprimir el enunciado y sus alternativas en pantalla
        # * funcion print_pregunta
        print_pregunta(enunciado, alternativas)
        respuesta = input('Escoja la alternativa correcta:\n> ').lower()

        """
        validate(opciones, eleccion)
        Args:
            opciones: [LIST] Ejemplo ["0", "1"]
            eleccion: STRING 
        Return:
            Manejo Error - input("Ingrese opción válida")
            eleccion
        """
        # * Aplicar validate([], "res")
        # todo: 7. Validar la respuesta entregada
        respuesta = validate(["a", "b", "c", "d"], respuesta)

        """
        verificar(alternativas, eleccion)
            Args:
                alternativas: [LIST] 
                eleccion: STRING  Ejemplo: "b"
            Return:
                BOOLEAN
        """
        # todo: 8. Verificar si la respuesta es correcta o no / verificar(alternativas, respuesta)
        # alternativas -> [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]],  "b"
        correcto = verificar(alternativas, respuesta)
        print(correcto)

        if correcto and n_pregunta < 3*p_level:
            print('Muy bien sigue así!')
            continuar = input('Desea continuar? [y/n]: ').lower()

            """
            validate(opciones, eleccion)
            Args:
                opciones: [LIST] Ejemplo ["0", "1"]
                eleccion: STRING
            Return:
                Manejo Error - input("Ingrese opción válida")
                eleccion
            """
            # * Aplicar validate([], "")
            # todo: 9. Validar si es que se responde y o n
            continuar = validate(["y", "n"], continuar)

            os.system(op_sys)
        elif correcto and n_pregunta == 3*p_level:
            print(f'Felicitaciones, Has respondido {
                  3*p_level} preguntas correctas. \n Has ganado la Trivia \n Gracias por Jugar, hasta luego!!!')
            time.sleep(3)
            os.system(op_sys)
        else:
            print(f'Lo siento, conseguiste {
                  n_pregunta - 1} respuestas correctas,\n Sigue participando!!')
            time.sleep(3)
            exit()
    else:
        print('Nos vemos la proxima vez, sigue practicando')
        time.sleep(3)
        exit()
