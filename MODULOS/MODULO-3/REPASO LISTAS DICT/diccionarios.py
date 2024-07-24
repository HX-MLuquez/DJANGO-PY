modelo_mascota = {
    "nombre": "Boby",
    "edad": "21",
    "email": "test@gmail.com",
    "raza": "",
    "vacunas": []
}

# Agregar
modelo_mascota["peso"] = "vacío"
# Modificar
modelo_mascota["raza"] = "soy un doberman"
# Eliminar
modelo_mascota.pop("edad")

# Recorrer el dict e imprimir cada una de sus elementos
for k, v in modelo_mascota.items():
    print(f'{k} - {v}')

print(modelo_mascota)


modelo_error = {
    "nombre": "",
    "edad": "",
    "raza": "",
    "vacunas": []
}

print(modelo_mascota.get("email", "No registra email de contacto"))
print(modelo_error.get("email", "No registra email de contacto"))


# Agregar
# Modificar
# Eliminar
