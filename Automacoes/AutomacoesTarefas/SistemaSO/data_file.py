from pathlib import Path
from pprint import pprint
from datetime import datetime

# Criando nosso diretório
path = Path('Automacoes/AutomacoesTarefas/SistemaSO/dados', 'new-teste.txt')

# Trazendo informações sobre o tempo 
print(path.stat()) # st_ctime='' é um metadado a respeito do tempo em que foi criado o path

stats = path.stat()
# Passando o dado especifico que precisamos, no caso o st_ctime['']
second_created = stats.st_ctime
# Função que interpreta o st_ctime, 'fromtimestamp' nos tras do st_ctime a hora e a o dia
# da criação do arquivo.
date_created = datetime.fromtimestamp(second_created)
print(date_created)
# Formatando o formato da apresentação dos dados presentes em date_created
format_date = date_created.strftime('%Y-%m-%d_%H_%M_%S')
print(format_date)