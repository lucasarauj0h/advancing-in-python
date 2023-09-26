import re

text = 'OneBitCode: Transformamos pessoas em programadores sem limites'

# 1 - índice inicial e final de palavras
# O r significa que estamos trabalhando com uma string bruta (raw string)

match = re.search(r'pessoas em programadores', text) 
#procure o 1º parametro no 2º parametro
print('Índice inicial', match.start())
print('Índice inicial', match.end())

# 2 - Achando uma lista de caracteres dentro de uma frase
pattern = '[a-m]'
result = re.findall(pattern, text) #cria uma lista com todos os caracteres
#presentes dentro do intervalo em que foi passado no argumento, de acordo
#com sua presença na lista
print(text, result) 

# 3 - verificando o inicio de uma string
rule = r'^O' 
phrases = ["A casa está suja", "O dia está lindo", "Vamos passear"]
for f in phrases: #rode um a um item/index da lista
    if re.match(rule, f): #caso o item da lista comece com a regra (A), printe
        print(f'Corresponde: {f}')
    else:
        print(f'Não corresponde: {f}') 
        
# 4 - verifique o fim da string
end = r'!$'
phrases2 = ["A casa está suja", "O dia está lindo!", "Vamos passear"]
for i in phrases2:
    match = re.search(end, i)
    if match:
        print(f'"{i}" corresponde ao 4-')
        