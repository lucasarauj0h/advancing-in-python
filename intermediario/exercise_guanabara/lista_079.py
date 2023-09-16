'''
Exercício Python 079: Crie um programa onde o usuário possa digitar 
vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro
ele não será adicionado. No final, serão exibidos todos os valores 
únicos digitados, em ordem crescente.
'''

import random 
verify = False
seguro = 0
lista = []
for i in range(10):
    num = random.randrange(10)
    # print(num)
    for index in range(len(lista)):
        if num == lista[index]:
            print(f'número {num} já adicionado a lista')
            verify = True

    if verify == False:
        lista.append(num)
        print(f'número {num} está correto!')
    verify = False

print(lista)
menor = 888888
save = []

for i in lista:
    for index in range(len(lista)):
        if lista[index] < menor:
            menor = lista[index]
         

for num in lista:
    index = 0
    for i in range(len(save)):
        if num > save[i]:
            index +=1
    save.insert(index, num)
    print(f'número {num} adicionado na posição {index} da lista')
    print(save)

print(f'{menor} .... menor número')
print(save)
