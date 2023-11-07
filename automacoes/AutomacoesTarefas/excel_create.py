from openpyxl import Workbook 
# Woorkbook é a "tabela" do excel, ou arquivo xlsx

# 1 - Criando o workbook
wb = Workbook() # Instanciando o workbook
name = 'automacoes\AutomacoesTarefas\primeira_tabela.xlsx'

# 2 - Utilizando a worksheet
# worksheet é a janela do excel, uma tabela, o nome sheet e o work é pq estamos trabalhando nela
ws1 = wb.active
ws1.title = 'Planilha1'

# Passando uma lista de listas
data = [
    ['Ano', 'Lucro', 'Custos'],
    [2021, '25%', '45%'],
    [2022, '45%', '55%'],
    [2023, '70%', '40%'],   
]
print(data)

# Cada virgula forma uma coluna, portanto uma lista de listas formam varias linhas e colunas
# Dessa maneira, quando eu adiciono o indice [0] da lista global, ela adiciona 
# uma serie de colunas, separadas pela virgula
for line in data:
    ws1.append(line)
    
# Criando uma nova tabela na planilha, uma sheet chamada "pi"
# Atribuindo valor na célula "D2"
ws2 = wb.create_sheet(title="Pi")
ws2['D2'] = 3.14
    
    
# Criando o arquivo em xlsx
wb.save(filename=name)



