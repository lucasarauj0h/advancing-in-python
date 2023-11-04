'''
## Organizador de Arquivos

1. Nesse exercício vamos colocar em prática o que aprendemos nas aulas anteriores. 
2. O seu desafio é criar um programa em Python que organiza arquivos de acordo com os seguintes tipos de arquivo:
- exe
- csv
- jpg
- pdf
- zip
- pbix
- xlsx
'''

import os

# 1 - Temos que acessar o diretório para organiza-lo, vamos ao diretório raiz do SO
base_path = os.path.expanduser('~')
print(base_path)

# 2 - Navega no diretório de destino.

path = os.path.join("C:\\Users\\Lucas\\OneDrive\\Área de Trabalho\\Excel estudo\\Power BI")
print(path)
work_dir = os.chdir(path)

# 3 - Lista arquivos do diretório
list_files = os.listdir(work_dir)
for i in list_files:
    print(i)
    
# 4 - Criar pastas para organizar arquivos.
type_files = ['exe', 'csv', "jpg", "pdf" , "zip", "pbix", "xlsx"]
for type in type_files:
    print(type)
    if type not in os.listdir():
        os.mkdir(type)
        
# 5 - Organizando os arquivos:

for file in list_files:
    for type in type_files: 
        if '.'+type in file:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type, file)
            os.replace(old_path, new_path)