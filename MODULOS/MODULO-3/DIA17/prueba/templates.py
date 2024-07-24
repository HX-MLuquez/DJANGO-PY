from string import Template 


# hacen las variables

html_template = Template('''
                       <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
</head>
<body>
$body    
</body>
</html>
         
                         ''')

div_template = Template('''<div>
                        <h2>$title1<h2>
                        <h3>$title2<h3>
                        <img src="$url">
                        </div>
                        ''')
texto = div_template.substitute(title1="hola", title2="hi", url="http:sarasa")

# -> '<div><h2>hola<h2><h3>hi<h3><img src="http:sarasa"></div>'

texto += div_template.substitute(title1="fe", title2="de", url="http:di")

# -> '<div><h2>hola<h2><h3>hi<h3><img src="http:sarasa"></div><div><h2>fe<h2><h3>de<h3><img src="http:di"></div>'
                      
