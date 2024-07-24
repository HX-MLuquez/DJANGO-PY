

i = 1
acumula = 0

while i <= 10:
    print(f'--> {acumula}')
    acumula += i 
    i += 1
print(f"El resultado acumulado final es {acumula}")
    
"""
acumula   |    i
--> 0     |   1
--> 1     |   2
--> 3     |   3
--> 6     |   4
--> 10    |   5
--> 15    |   6
--> 21    |   7
--> 28    |   8
--> 36    |   9
--> 45    |   10
"""