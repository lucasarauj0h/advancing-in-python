'''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão 
qualquer que use parênteses. Seu aplicativo deverá analisar 
se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expressao = str(input("digite a sua expressão: "))
contagem = []
entrada = 0
saida = 0
for i in expressao:
    if i == '(':
        contagem.append('(')
    if i == ')':
        contagem.pop()

print(contagem)
if len(contagem) == 0: 
    print('A expressão está correta.')
else:
    print('A expressão está incorreta')