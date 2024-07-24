import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad /#* POOL p.pool_preguntas[dificultad]
    preguntas = 
    
    # usar opciones desde ambiente global
    global 
    # escoger una pregunta /#* random.choice()
    n_elegido = 
    # eliminarla del ambiente global para no escogerla de nuevo /#* .remove(n_elegido)
    
    
    # escoger enunciado y alternativas mezcladas
    pregunta = # Ejemplo de lo que se debe armar: 'pregunta_1'
    
    #* shuffle_alt() IN pregunta OUTPUT [random de alternativas]
    alternativas = # Implementar shuffle_alt()<- recibe ¿?
    
    
    return pregunta['enunciado'], alternativas

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