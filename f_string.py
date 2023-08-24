#f-string, vamos entender. 
nome = 'lucas de araujo souza'
altura = 14894893646.73
altura2 = 1.73
peso = 70
imc = peso / altura2 ** 2

linha_1 = f'{nome} tem {altura:,.2f} de altura e {peso} de peso'
linha_2 = f'seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)
print('b aaaa')