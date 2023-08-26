"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = 'Olha só que, coisa interessante'
lista_palavra = frase.split() #quebra e divide as palavras nos espaços
print(lista_palavra)

lista_palavra = frase.split(', ') #quebra e divide na virgula
print(lista_palavra)