from pathlib import Path
from pprint import pprint

# Criando nosso diretório
root_dir = Path('Automacoes/AutomacoesTarefas/SistemaSO/dados')
file_paths = root_dir.iterdir()
# print(root_dir)


# pprint(list(file_paths))
# Vendo todos os arquivos presentes no diretório e acessando-os um a um 
for path in file_paths:
    # Criando o novo nome dos arquivos para cada arquivo presente no diretório 
    new_filename = f'ne {path.suffix}'
    print(new_filename)
    # Juntando o diretório + o novo nome do arquivo
    new_filepath = path.with_name(new_filename)
    print(new_filepath)
    # Para alterar seu nome, eu preciso passar também o seu diretório para que se converse
    # o lugar atual em que se encontra o arquivo. Caso eu passe diretamente o 
    # path.rename(new_filename) ele irá trocar apenas o nome do arquivo pra 
    # new-teste.txt e jogará no repositório global desse escopo
    # portanto temos que passar como argumento 
    # Automacoes\AutomacoesTarefas\SistemaSO\dados\new-teste.txt
    
    path.rename(new_filepath)
    
    # print(path.stem)
    # print(path.suffix)