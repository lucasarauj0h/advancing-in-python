"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input("digite um número: ")

if numero_str.isdigit(): #verifica se a var str é um número inteiro. se sim retorna true
    numero_float = float(numero_str) 
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Isso não é um número')

try:
    print(f'STR: {numero_str}')
    numero_float = float(numero_str)
    print(f'FLOAT: {numero_str}') 
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except: 
    print('isso não é um float')
    ...