"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

   Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
"""

multiply = 10
soma = 0
cpf_original = str('74682489070')
cpf = cpf_original[:9]

for i in range(9):

    soma += int(cpf[i])*multiply
    print(f'digito: {cpf[i]}, multiplo {multiply}, valor {int(cpf[i])*multiply}, soma {soma}')
    multiply -= 1

mult = soma*10
sobra = mult%11
teste = sobra if sobra <=9 else 0 
print(sobra)
print(sobra if sobra <=9 else 0 )

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

soma = 0
cpf_teste2 = str(cpf)+str(sobra)
print(cpf_teste2)
multiply = len(cpf_teste2)
for i in range(len(cpf_teste2)):

    soma += int(cpf_teste2[i])*multiply
    print(f'digito: {cpf_teste2[i]}, multiplo {multiply}, valor {int(cpf_teste2[i])*multiply}, soma {soma}')
    multiply -= 1

mult = soma*10
sobra2 = mult%11
teste2 = sobra2 if sobra2 <=9 else 0
print(sobra2)
print(sobra2 if sobra2 <=9 else 0 )
print(f'{teste}, {cpf_original[9]}, {teste2}, {cpf_original[10]}')


if teste == int(cpf_original[9]) and teste2 == int(cpf_original[10]):
    print("CPF válido!")
else:
    print("CPF inválido.")

print("teste")