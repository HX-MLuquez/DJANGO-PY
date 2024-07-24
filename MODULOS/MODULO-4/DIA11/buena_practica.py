

try:
    archivo = open('sarasa.txt')
    contenido = archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado")
except Exception as e:
    print(e)
finally:
    if archivo:
        archivo.close()

# -------------------------------------------------------------

with open("sarasa.txt") as file:
    try:
        print("...")
    except Exception:
        print("Error")
