

def cuadrado_cubo(base):
    cuadrado = base**2
    cubo = base**3
    return cuadrado, cubo, 101


print(cuadrado_cubo(2)) # -> tuple -> (4, 8, 101)

a,b,c = cuadrado_cubo(2)

print(c)
