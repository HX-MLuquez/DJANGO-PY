import requests
import json
from string import Template


response = json.loads(requests.get(
    "https://jsonplaceholder.typicode.com/photos").text)[:5]

# print(response)
lista_url = []
for p in response:
    # print(p["url"])
    lista_url.append(p["url"])

print(lista_url)

html_template = Template('''
                        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>APP</title>
</head>
<body>
<h1>APP APIS</h1>
$body
</body>
</html>
                         ''')

texto_img = ''
img_template = Template('<img src="$url">')
# imagen = img_template.substitute(url= "https://via.placeholder.com/600/92c952")

for posteo in lista_url:
    texto_img += img_template.substitute(url=posteo) + '\n'

"""
texto_img '''
<img src="https://via.placeholder.com/600/92c952">
<img src="https://via.placeholder.com/600/771796">
<img src="https://via.placeholder.com/600/24f355">
<img src="https://via.placeholder.com/600/d32776">
<img src="https://via.placeholder.com/600/f66b97">
          '''
"""
print(texto_img)

html_original = html_template.substitute(body=texto_img)

print(html_original)

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_original)

