def agregar_ingrediente(ingredientes_orden, seleccionado):

    bandera = "s"
    while bandera == "s":
        
        disponibles = ['Aceituna', 'Ananá', 'Palmito', 'Jamón']
       
        seleccionado = disponibles[seleccionado-1]
        if seleccionado in ingredientes_orden['ingredientes']:
            print("Ese ingrediente ya está en la lista")
        else:
            ingredientes_orden['ingredientes'].append(seleccionado)
            print(f'Se ha agregado el nuevo ingrediente {seleccionado}')
        bandera = input("Quieres agregar otro? [s/n]")
    return ingredientes_orden
