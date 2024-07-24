

estimulos = input("Responde a los estímulos? [y/n]  ").lower()

if estimulos == "y":
    print("Valora la necesidad de llevarlo al Hospital más cercano")
else:
    print("Abrir la vía aéra")
    respira = input("Respira? [y/n]  ").lower()
    if respira == "y":
        print("Permitirle posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a Ambulancia")
        ambulancia = "n"
        while ambulancia == "n":
            signos = input("Tiene signos de vida? [y/n]  ").lower()
            if signos == "n":
                print("Aplicar compresiones toráxicas hasta que llegue ambulancia")
            else:
                print("Reevaluar a la espera de la Ambulancia")
            ambulancia = input("Llegó la ambulancia? [y/n]  ").lower()
            
print("Programa finalizado")