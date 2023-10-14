from pathlib import Path
from pprint import pprint

# Criando um caminho/diretório, o 1º parametro é a pasta, o 2º é o arquivo
p1 = Path('Automacoes/AutomacoesTarefas/SistemaSO/dados', 'teste.txt') 
print(p1)
print(type(p1))
print(p1.name) # Nome do arquivo
print(p1.stem) # Nome do arquivo antes do tipo do arquivo
print(p1.suffix) # Nome do tipo do arquivo
print(p1.exists()) # Retorna [True] se o arquivo existe ou [False] para não

if p1.exists():
    with open(p1, 'r', encoding='utf-8') as file:
        print(file.read())
        
p2 = Path('basic')
pprint(list(p2.iterdir()))