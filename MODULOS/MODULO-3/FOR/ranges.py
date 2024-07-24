#* RANGE
print(type(range(4,10,2))) # <class 'range'>
print(range) # <class 'range'>

print(range(5)) # range(0, 5)

print(range(2, 5)) # range(2, 5)

for i in range(5):
    print(f'range(5) -> {i}')
# range(5) -> 0
# range(5) -> 1
# range(5) -> 2
# range(5) -> 3
# range(5) -> 4

for i in range(2, 5):
    print(f'range(2, 5) -> {i}')
# range(2, 5) -> 2
# range(2, 5) -> 3
# range(2, 5) -> 4

#                     intervalos -> va saltando en este caso de 3 en 3
for i in range(2, 10, 3):
    print(f'range(2, 10, 3) -> {i}')
# range(2, 10, 3) -> 2
# range(2, 10, 3) -> 5
# range(2, 10, 3) -> 8
