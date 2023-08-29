# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Araujo 4',
    'sobrenome': 'Araujo 3',
    'sobrenome': ('Araujo 2', 'Souza 2', 'Laranja', 'Uncle'),
}

print(len(pessoa)) #quantas keys/chaves tenho no dicionario.
print(pessoa.keys()) #aparece só as chaves
print(tuple(pessoa.keys())) #tranformando somente as chaves em tuplas
print()

print(pessoa.values()) #aparecendo somente os valores.
print(tuple(pessoa.values())) #tranformando somente os valores em tuplas
print()

print(pessoa.items()) #aparecendo as kyes e os valores em tupla.
#em items, temos o indice 0, 1, 2, 3, ...
print()

for key, it in pessoa.items():
    print(f'key: {key} ->  value: {it}')

print()


print(f'antes do .setdefault -> {pessoa.get("idade")}') #como não existe nenhuma key 'idade'
#no dicionario pessoa
#ele atribui o valor como "none" automaticamente, mas podemos adicionar um valor padrão
pessoa.setdefault('idade', 0)
print(f'depois do .setdefault -> {pessoa.get("idade")}')
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')

print()
print()
print()
print()

teste = {
    'key_one': 1,
    'key_two': 2,
    'list': [5,6,7,8,9],
}

d2 = teste #como é mutavel, o sinal de igual diz que d2 está apontando para teste
#e não que tem o valor de teste, apenas que aponta para teste.

#caso eu altere d2, o teste será alterado tambem pois os dois são o mesmo item!

#d2['key_one'] = 100

#print(teste)

#para concertar isso usamos .copy()

d3 = teste.copy()

d3['key_one'] = 157
d3['list'][0] = 157
print(d3, teste)
#porem com o copy, os dados mutaveis como listas continuam com esse problema. 
#para resolver esse problema, usamos o deep copy
import copy

print()
print()

teste = {
    'key_one': 1,
    'key_two': 2,
    'list': [5,6,7,8,9],
}

d3 = copy.deepcopy(teste)
d3['key_one'] = 157
d3['list'][0] = 157
print(d3, teste)

print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')

print()
print()
print()
print()

p1 = {
    'nome': 'Lucas',
    'sobrenome': 'Araujo',
}

print(p1.get('nome', 'não existe')) #caso não exista um get nome, ao inves de retornar 
#none, ele retornara a mensagem que deixamos a ele. nesse caso 'nao existe'.

# nome = p1.pop('nome') #elimina a chave nome, mas retorna o valor contido nessa key
# print(nome)

ultima_chave = p1.popitem() #elimina o ULTIMO item do dicionario
print(ultima_chave)
print(p1)
print()
print()
print()
print()
p1 = {
    'nome': 'Lucas',
    'sobrenome': 'Araujo',
}

#.update realiza uma atualização no dicionario. pode criar nova key um mudar uma existente
p1.update({
    'nome': 'Luas',
    'idade': 20,
     
})
print(p1)
p1.update(nome='Luz',idade=78)
print(p1)
tupla = ('nome', 'lLucas'), ('idade', '77')
p1.update(tupla)
print(p1)
