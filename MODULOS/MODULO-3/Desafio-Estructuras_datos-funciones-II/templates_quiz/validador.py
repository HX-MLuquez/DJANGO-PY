
def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
   # pass
    
    # ["0", "1"]  -  "1"
    # if "2" in ["1","2","3"]
    # if eleccion in opciones
    while 1:
        eleccion = input("")
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
