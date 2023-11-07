from openpyxl import load_workbook

# 1 - Lendo o workbook
wb = load_workbook(filename='automacoes\AutomacoesTarefas\primeira_tabela.xlsx')
pi = (wb['Pi'])
planilha1 = (wb['Planilha1'])

# 2 - Acessando o valor de uma determinada célula
print(planilha1['B2'].value) # - temos que informar o .value para que exiba o valor da celula

# 3 - Iterando valores por meio de loops
for i in range(1, 4+1):
    # print(f"{planilha1['A{i}'].value}, a {i}")
    print(planilha1['A%s' %i].value, end=' ')
    print(planilha1['B%s' %i].value, end=' ')
    print(planilha1['C%s' %i].value)