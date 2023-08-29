# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista.sort() #ordena a lista do menor para o maior.
print(lista)
lista.sort(reverse=True) #inverte a lista, do maior para o menor
print(lista)
print()
print()
print()
#.sort funciona com numeros e letras, mas contem algumas limitações. ele não sabe 
#ordenar dicionarios.
# sorted(lista) #mesma coisa que a função sort
# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Airanda'},
    {'nome': 'Luiz', 'sobrenome': 'Oliveira'},
    {'nome': 'Luiz', 'sobrenome': 'Silva'},
    {'nome': 'Luiz', 'sobrenome': 'Moreira'},
    {'nome': 'Luiz', 'sobrenome': 'Souza'},
]
#o python não sabe como ordernar os dicionarios, visto que eu nao há como definir 
#qual é maior que qual. portanto usamos uma função dentro do .sort()

def ordena(item):
    return(item['nome'])

def ordena_sobrenome(item):
    return(item['sobrenome'])

lista.sort(key=ordena) #dizemos para o sort que a chave, ou melhor
#como havia um dicionario com 2 lista, o sort não sabia qual era para deixar
#em ordem alfabetica, então a partir da funcao ordena, que retorna que a
#a chave é o nome do dicionario, ele separo para nos a partir da key
lista.sort(key=ordena_sobrenome)
for item in lista:
    print(item)

#ao inves de eu ter todo esse trabalho, eu poderia usar a função lambda
print()
print()
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(item):
    for item in l2:
        print(item)
    print()

lista.sort(key=lambda item: item['nome'])
for item in lista:
    print(item)

print()
print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
print('-------------------- SOBRENOME --------------------')
exibir(l2)


