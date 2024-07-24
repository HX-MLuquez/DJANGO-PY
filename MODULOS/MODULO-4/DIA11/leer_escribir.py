

try:
    edad = int(input("Ingrese edad: "))
except Exception as e:
    with open('./utils/mimi2.log', 'r+') as file: #! FileNotFoundError: error
        file.write(f'ERROR: {e}')
        
