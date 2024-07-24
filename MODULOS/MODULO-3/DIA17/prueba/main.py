

# import templates + peticiones

# def -> peticion recorre datos crea muchos divs . 
# los inserta en el body y este resultado lo usa para escribir nuestro .html

import requests
import json 
import templates as t 
from peticiones import req

# response = json.loads(requests.get('https://aves.ninjas.cl/api/birds').text)
# print(response[0]["images"]["main"])

# for element in response:
#     print(element["images"]["main"])
    
    
# with open  -> "w" -> index.html
html_result = t.html_template.substitute(body= '<h2></h2>')

if __name__ == '__main__':
    
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(html_result)