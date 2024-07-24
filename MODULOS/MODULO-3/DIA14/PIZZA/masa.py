
def cambiar_masa(ingredientes_orden):
    # Masa Tradicional, Masa Delgada, Masa con Bordes de Queso
    tipo_masa = input("""¿Qué tipo de masa quieres?
                            A) Masa Tradicional
                            B) Masa Delgada
                            C) Masa con Bordes de Queso
                            """).upper()
    if tipo_masa == "A":
        ingredientes_orden["masa"] = "Masa Tradicional"
    elif tipo_masa == "B":
        ingredientes_orden["masa"] = "Masa Delgada"
    elif tipo_masa == "C":
        ingredientes_orden["masa"] = "Masa con Bordes de Queso"
    # else:
    #     ingredientes_orden["masa"] = "Masa Tradicional"

    if tipo_masa in ["A", "B", "C"]:
        print(f'Su masa se cambió a {ingredientes_orden["masa"]}')
    else:
        print(f'Su masa no se pudo cambiar')

    return ingredientes_orden

# if __name__ == '__main__':
  