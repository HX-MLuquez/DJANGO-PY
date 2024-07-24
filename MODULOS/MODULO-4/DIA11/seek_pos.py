

with open('momo.log') as file:
    file.seek(8)
    print(file.read(10))