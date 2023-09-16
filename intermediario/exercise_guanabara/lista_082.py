'''Exercício Python 082: Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, crie duas listas extras que vão conter apenas os 
valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

import random 
total = 0
lista = []
save = []
pares = []
impares = []

for i in range(random.randrange(10)):
    lista.append(random.randrange(10))

for num in lista:
    index = 0
    if num % 2 == 0:
        for ind in range(len(pares)):
            if num > pares[ind]:
                index += 1
        pares.insert(index, num)
    else: 
        for ind in range(len(impares)):
            if num > impares[ind]:
                index += 1
        impares.insert(index, num)

print(lista)
print(pares)
print(impares)