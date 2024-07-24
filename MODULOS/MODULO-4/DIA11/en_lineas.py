

pagina = open("test.html")
lineas = pagina.readlines()

print(lineas)

pagina.close()

# [ '<!DOCTYPE html>\n', '<html lang="en">\n', '<head>\n', '    <meta charset="UTF-8">\n', '    
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n', '    
#    <title>Test</title>\n', '</head>\n', '<body>\n', '    
#    <h1>Vamos a controlar este archivo</h1>\n', '</body>\n', '</html>' ]