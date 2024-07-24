

import os 

antiguo = os.path.join("utils", "otro.txt")
print(antiguo)
nuevo = os.path.join("utils", "hola_mundo.html")

os.rename(antiguo, nuevo)
