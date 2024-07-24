from string import Template


html_general = Template('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
</head>
<body style="font-family: sans-serif;">
    <h1 style="text-align: center;">Aves de Chile</h1>
    <div style="display: flex; flex-wrap: wrap; justify-content: center;">
        $body
    </div>
</body>
</html> 
''')

element_template = Template('''
<div style="text-align: center; padding: 6px; margin: 10px; width: 250px; background-color: rgba(205, 237, 210, 0.892);">
    <h2>$title_es</h2>
    <h3>$title_en</h3>
    <img src="$url" alt="" style="height: 180px; width: 150px;">
</div> 
''')
