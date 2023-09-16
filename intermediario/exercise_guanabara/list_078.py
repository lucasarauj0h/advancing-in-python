#Exercício Python 078: Faça um programa que leia 5 valores numéricos e 
#guarde-os em uma lista. No final, mostre qual foi o maior e o 
#menor valor digitado e as suas respectivas posições na lista. 

lista = []
max = 0
min = 0
teste = (5,7,8)


for i in range(5):
    lista.append(int(input(f"Digite um valor para a posição {i} ----> ")))
    if i == 0:
        max = lista[i]
        min = lista[i]
    if max < lista[i]:
        max = lista[i]
    elif min > lista[i]:
        min = lista[i]

print(lista)
print(f'números digitados: {lista}')
print(f'O maior número digitado foi {max} nas posições ', end='')
for i, v in enumerate(lista):
    if v == max:
        print(f'{i}... ', end='')
print()
print(f'O menor número digitado foi {min} nas posições ', end='')
for i, v in enumerate(lista):
    if v == min:
        print(f'{i}...', end='')   