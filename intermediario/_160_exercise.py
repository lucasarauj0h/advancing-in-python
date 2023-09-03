# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

print(produtos[0]['preco'])

for i in range(len(produtos)):
    
    novo_valor = round((float(produtos[i]['preco'])*1.10),2)
    produtos[i].update(preco=novo_valor)


    # produtos[i].values()

# for i in range(len(produtos)):
    # print(produtos[i])


def ordena_nome(item):
    return item['nome']

def ordena_preco(item):
    return item['preco']

produtos.sort(key=ordena_nome, reverse=True)
# print(produtos)

import copy 

produtos_ordenados_nome = copy.deepcopy(produtos)

produtos.sort(key=ordena_preco)
# print(produtos)

produtos_ordenados_preco = copy.deepcopy(produtos)

for i in range(len(produtos)):
    print(produtos_ordenados_nome[i])

print()
print('--------------------------')
print()

for i in range(len(produtos)):
    print(produtos_ordenados_preco[i])

    