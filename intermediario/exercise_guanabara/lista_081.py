'''
Exercício Python 081: Crie um programa que vai ler vários
números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

import random 
total = 0
lista = []
save = []
for i in range(random.randrange(10)):
    lista.append(random.randrange(10))
    total += 1

for i in lista:
    index = 0
    for ind in range(len(save)):
        if i < save[ind]:
            index += 1
    save.insert(index, i)
    if i == 5:
        print(f'número 5 no indice {lista.index(5)}')




print(lista)
print(save)



