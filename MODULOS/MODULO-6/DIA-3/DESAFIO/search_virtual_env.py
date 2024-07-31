import os


def find_virtualenvs(base_path):
    virtualenvs = []
    for root, dirs, files in os.walk(base_path):
        if 'bin' in dirs and 'activate' in os.listdir(os.path.join(root, 'bin')):
            # virtualenvs.append(root)
            env_name = os.path.basename(root)
            virtualenvs.append(env_name)
        elif 'Bin' in dirs and 'activate' in os.listdir(os.path.join(root, 'Bin')):
            # virtualenvs.append(root)
            env_name = os.path.basename(root)
            virtualenvs.append(env_name)
        elif 'Scripts' in dirs and 'activate' in os.listdir(os.path.join(root, 'Scripts')):
            # virtualenvs.append(root)
            env_name = os.path.basename(root)
            virtualenvs.append(env_name)
    return virtualenvs


base_path = 'C:/Users/mauuu/OneDrive/Escritorio/DJANGO-PY 2024/MODULOS/MODULO-6/DIA-3/DESAFIO'
envs = find_virtualenvs(base_path)
print(f"Entornos virtuales encontrados: {envs}")


#* PASO a PASO
# 1. Copiar PATH
# C:/Users/mauuu/OneDrive/Escritorio/DJANGO-PY 2024/MODULOS/MODULO-6/DIA-3/DESAFIO/search_virtual_env.py

#2. De tener / pasar a /
# Select / -> ctrol + f
# / -> / pytz==2019.3

# C:\Users\mauuu\OneDrive\Escritorio\DJANGO-PY 2024\MODULOS\MODULO-6\DIA-3\DESAFIO