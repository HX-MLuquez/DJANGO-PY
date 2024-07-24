
#  [{}{}{}{}{}] <- Modelo + típico de datos 
#  [{{[{},{},{}]}{}}]
#* FOR normal
students1 = [
    {"name": "Alice", "age": 23, "grade": "A"},  # pos 0
    {"name": "Bob", "age": 22, "grade": "B"},    # pos 1
    {"name": "Charlie", "age": 24, "grade": "C"},# pos 2
    {"name": "David", "age": 21, "grade": "A"}   # pos 3
]
print(f'nombre: {students1[2]["name"]} y grado {students1[2]["grade"]}') # nombre: Charlie y grado C

gradeA = []

for student in students1:
    print(student)
    if student["grade"] == "A":
        data_student ={
            "name": student["name"],
            "grade": student["grade"]
        }
        gradeA.append(data_student)

print(f'Los alumnos en grado "A" son {gradeA}') # ->  [{'name': 'Alice', 'age': 23, 'grade': 'A'}, {'name': 'David', 'age': 21, 'grade': 'A'}]

#         0                                         1 2 3 4
# [ (0, {"name": "Alice", "age": 23, "grade": "A"})         ]