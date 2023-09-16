'''Exercício Python 080: Crie um programa onde o usuário possa 
digitar cinco valores numéricos e cadastre-os em uma lista, já 
na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.'''

import random 
lista =[]

for i in range(5):
    num = random.randrange(10)
    index = 0
    for i in range(len(lista)):
        if num > lista[i]:
            index +=1
    lista.insert(index, num)
    print(f'número {num} adicionado na posição {index} da lista')

print(lista)
    
            