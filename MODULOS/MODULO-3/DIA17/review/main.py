from req_get import request_get
import templates as tem

def build_app(url):
    pajaros = request_get(url)
    # print(response)
    etiqueta_texto_concatenadas = ''

    for pajaro in pajaros:
        # print(pajaro)
        etiqueta_texto_concatenadas += tem.element_template.substitute(
            title_es=pajaro['name']['spanish'],
            title_en=pajaro['name']['english'],
            url=pajaro['images']['main']
        )

    html_base = tem.html_general.substitute(body=etiqueta_texto_concatenadas)
    return html_base

# html_base = tem.html_general.substitute(body='<h2>Hola Mundo!!!</h2>')


if __name__ == "__main__":
    print("__Init__")
    html = build_app("https://aves.ninjas.cl/api/birds") # en html guardo lo que retorna build_app(...)
    
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(html)

    # print(build_app("https://aves.ninjas.cl/api/birds"))


"""
etiqueta_texto_concatenadas
'''
<div style="text-align: center; padding: 6px; margin: 10px; width: 250px; background-color: rgba(205, 237, 210, 0.892);">
    <h2>1</h2>
    <h3>1</h3>
    <img src="1" alt="" style="height: 180px; width: 150px;">
</div> 
<div style="text-align: center; padding: 6px; margin: 10px; width: 250px; background-color: rgba(205, 237, 210, 0.892);">
    <h2>2</h2>
    <h3>2</h3>
    <img src="2" alt="" style="height: 180px; width: 150px;">
</div> 
<div style="text-align: center; padding: 6px; margin: 10px; width: 250px; background-color: rgba(205, 237, 210, 0.892);">
    <h2>3</h2>
    <h3>3</h3>
    <img src="3" alt="" style="height: 180px; width: 150px;">
</div> 
'''
"""
