from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

total = 0

def function_reduce(total, product):
    print(total+product['preco']) #mostrando o acumulador
    return total+product['preco']

total = reduce(
    function_reduce, #função que executa o reduce
    produtos, #parametro da função
    0 #valor inicial da função 
)

#o modulo reduce passa por cada index da lista produtos. 
#dentro da função passada como patramentro, passamos o total (acumulador) e a lista
#como argumento. dentro da função, pega-se o total acumulado e soma-se ao valor do 
#preço vinculado ao index atual, declarado pela lista + key da lista


# for p in produtos:
#     total += p['preco']

# print(total)