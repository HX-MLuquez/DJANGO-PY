

# with open("mi_archivo.txt", "a+") as file:
#     file.write("1° hola mundo \n")
#     file.write("2° bye bye mundo \n")

#     file.seek(0)

#     contenido = file.read()
#     print(contenido)

from datetime import datetime
with open("mi_archivo.txt", "a+") as log:
    log.seek(0)
    print(log.read())
    now = datetime.now()
    log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: \n")
    log.seek(0)
    print(log.read())
