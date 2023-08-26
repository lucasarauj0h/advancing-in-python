import random
import sys

multiply = 10
soma = 0
#cpf_original = '746824890'.replace('.','').replace('-','')
#cpf = cpf_original[:9]
cpf = ''
for i in range(9):
    cpf += str(random.randint(0,9))
    print()

print(f'printando cpf {cpf}')
for i in range(9):

    soma += int(cpf[i])*multiply
    print(f'digito: {cpf[i]}, multiplo {multiply}, valor {int(cpf[i])*multiply}, soma {soma}')
    multiply -= 1

sobra = (soma*10)%11
teste = sobra if sobra <= 9 else 0 
print(sobra)
print(sobra if sobra <= 9 else 0 )

print(f'testeando sobra {sobra}')

soma = 0
multiply=11

for i in range(9):

    soma += int(cpf[i])*multiply
    print(f'digito: {cpf[i]}, multiplo {multiply}, valor {int(cpf[i])*multiply}, soma {soma}')
    multiply -= 1
soma += sobra*2
sobra2 = (soma*10)%11

print(f'a sobra2 = {sobra2}')

teste2 = sobra2 if sobra2 <=9 else 0
cpf_original = str(cpf)+str(teste)+str(teste2)
print(sobra2)
print(sobra2 if sobra2 <=9 else 0 )

print(cpf_original)
print(f"Cpf gerado: {cpf}{teste}{teste2}")

#testado e comprovado.