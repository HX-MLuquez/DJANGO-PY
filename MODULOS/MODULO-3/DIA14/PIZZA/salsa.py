# Salsa de Tomate, Salsa Alfredo, Salsa Barbecue, Salsa Pesto

def cambiar_salsa(ingredientes_orden):
    tipo_masa = input("""¿Qué tipo de salsa quieres?
                            A) Salsa de Tomate
                            B) Salsa Alfredo
                            C) Salsa Barbecue
                            D) Salsa Pesto
                            """).upper()
    if tipo_masa == "A":
        ingredientes_orden["salsa"] = "Salsa de Tomate"
    elif tipo_masa == "B":
        ingredientes_orden["salsa"] = "Salsa Alfredo"
    elif tipo_masa == "C":
        ingredientes_orden["salsa"] = "Salsa Barbecue"
    elif tipo_masa == "D":
        ingredientes_orden["salsa"] = "Salsa Pesto"


    if tipo_masa in ["A", "B", "C", "D"]:
        print(f'Su salsa se cambió a {ingredientes_orden["salsa"]}')
    else:
        print(f'Su salsa no se pudo cambiar')

    return ingredientes_orden
