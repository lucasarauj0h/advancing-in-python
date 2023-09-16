from functools import partial
from types import GeneratorType

#partial é uma função que irá receber uma função, e um ou mais argumentos.
#queremos criar uma função que aumente em 10%


def print_iter(iterator):
    print(*list(iterator), sep='\n')


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def increase_percentage(product, percent):
    return round(product*percent, 2)

new_product = [
    {**p, 'preco': increase_percentage(p['preco'], 1.1)} for p in produtos if p['preco'] > 10
]
print_iter(produtos)
print('-'*30)
print_iter(new_product)

print('-'*30)
new_product = filter(
    lambda p: p['preco']>100,
    produtos

)

print_iter(new_product)
