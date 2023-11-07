from openpyxl import Workbook 
# Woorkbook é a "tabela" do excel, ou arquivo xlsx

# 1 - Criando o workbook
wb = Workbook() # Instanciando o workbook
name = 'automacoes\AutomacoesTarefas\primeira_tabela.xlsx'

# 2 - Utilizando a worksheet
# worksheet é a janela do excel, uma tabela, o nome sheet e o work é pq estamos trabalhando nela
ws1 = wb.active
ws1.title = 'Planilha1'

file_txt = open('automacoes\AutomacoesTarefas\gastos.txt', 'r', encoding='utf-8').read()

# Deixando o nosso txt em uma lista de listas.
list_data = file_txt.splitlines()
# print(list_data)

for i in range(0, len(list_data)):
    print(list_data[i])
    list_data[i] = list_data[i].split(',')
    print(list_data[i])

for line in list_data:
    ws1.append(line)
    
# Criando o arquivo em xlsx
wb.save(filename=name)

