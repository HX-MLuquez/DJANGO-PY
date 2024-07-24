import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3], # <- [1,2]
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad): # -> 'basicas'
    #escoger preguntas por dificultad /#* POOL p.pool_preguntas[dificultad]
    preguntas = p.pool_preguntas[dificultad]

    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta /#* random.choice()
    n_elegido = random.choice(opciones[dificultad]) # <- 3
    # eliminarla del ambiente global para no escogerla de nuevo /#* .remove(n_elegido)
    
    opciones[dificultad].remove(n_elegido)
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas[f'pregunta_{n_elegido}'] # Ejemplo de lo que se debe armar: 'pregunta_1'
    """
    {'enunciado':['Enunciado básico 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
    """
    #* shuffle_alt() IN pregunta OUTPUT [random de alternativas]
    alternativas = shuffle_alt(pregunta) # Implementar shuffle_alt()<- recibe ¿?
    """
    [['alt_1', 0], 
     ['alt_3', 0], 
     ['alt_2', 1],
     ['alt_4', 0]]
    """
    
    return pregunta['enunciado'], alternativas
    # -> tuple   ['Enunciado básico 3'] , [['alt_1', 0], ['alt_3', 0], ['alt_2', 1],['alt_4', 0]]
if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')