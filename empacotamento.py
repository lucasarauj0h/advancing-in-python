a, b = 1,2
a, b = b, a
print(a,b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souzas',
}

print()
print("pessoa")
a, b = pessoa
print(a,b) #desse modo, é passado somente a chave. 
#caso eu use values, é passado o valor do dicionario
print()

print("pessoa.values()")
a, b = pessoa.values()
print(a,b)
print()

print("pessoa.items()")
(a1, a2), (b1, b2)= pessoa.items()
print(a1,a2)
print(b1,b2)


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souzas',
}

dados_pessoa = {
    'idade': 18,
    'altura': 1.75
}

print(pessoa, dados_pessoa)
print()

#desempacotamento de um dicionario aqui dentro
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

print()
print('------------------------------------------')
print()

def mostro_argumentos_nomeados(**kwargs):
    print(kwargs)

mostro_argumentos_nomeados(nome='Lucas', quite='22Als')

print()
print('------------------------------------------')
print()

def mostro_argumentos_nomeados(**kwargs):
    for key, arg in kwargs.items():
        print(key, arg)


mostro_argumentos_nomeados(nome='Lucas', quite='22Als')


mostro_argumentos_nomeados(**pessoa_completa)




