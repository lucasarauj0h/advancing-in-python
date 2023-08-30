# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=50)

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

lista = [
    numero * 2
    for numero in range(10)
    ]
print(lista)

print()
print('-------------------------------------------------')
print()

#mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    #{'nome': produto['nome'], 'preco': produto['preco']}
    {**produto, 'preco': produto['preco']*1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')

p(novos_produtos)


# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]

#


print()
print('-------------------------------------------------')
print()

lista = [n for n in range(10) if n<5] #realize a ação se n for menor que 50.

print(lista)

novos_produtos = [
    #{'nome': produto['nome'], 'preco': produto['preco']}
    {**produto, 'preco': produto['preco']*1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

p(novos_produtos)

#mapeamento: pegando um dado, jogando pra outra lista e alterando ou nao, mas de msm tamanho
