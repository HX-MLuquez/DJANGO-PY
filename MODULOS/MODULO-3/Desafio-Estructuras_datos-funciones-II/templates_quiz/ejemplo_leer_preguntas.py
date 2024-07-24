import preguntas as p


print(p.pool_preguntas['intermedias'])
# Es IGUAL a:
print(p.preguntas_intermedias)

# ya que pool_preguntas['intermedias'] == "preguntas_intermedias"

p.preguntas_basicas["pregunta_1"]["enunciado"][0]

for a in p.preguntas_basicas["pregunta_1"]["alternativas"]:
    if a[1] == 1:
        print("es la correcta")