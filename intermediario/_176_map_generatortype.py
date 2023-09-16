from functools import partial
from types import GeneratorType

#partial é uma função que irá receber uma função, e um ou mais argumentos.
#queremos criar uma função que aumente em 10%

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def print_iter(iterator):
    print(*list(iterator), sep='\n')

new_products = [
    {**p} for p in produtos #estou separando os dicionarios, 1 * - apenas as keys
    # 2 ** - keys e preços
]

# print_iter(new_products)

def increase_percentage(value, percent):
    return round(value*percent, 2)

percent = float(input('Qual a porcentagem que deseja aumentar o preço dos produtos? = '))
increase = partial(
    increase_percentage,
    percent=percent
)

new_products = [
    #{**p, 'preco': round(p['preco']*1.10, 2)} for p in produtos #estou separando os dicionarios, 1 * - apenas as keys
    {**p, 'preco': increase(p['preco'])} for p in produtos
    # 2 ** - keys e preços
    #estou sobreescrevendo os resultados da key preço;
]

print_iter(new_products)
# print(*list(produtos))

def change_price_products(product):
    
        return {**product,
            'preco': increase(product['preco'])
        }

#map é uma função que recebe outra função 
new_products_test = map(change_price_products, produtos)  

print('*' * 100)
print_iter(new_products_test)

print(
    list(map(
        lambda x: x*3,
        [1,2,3,4]))) #a função map faz um for que passa automaticamente, todos os valores
        #presentes na lista, dessa forma passara por cada item da lista. será atribuido 
        #ao valor x
