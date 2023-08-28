"""
Closure e funções que retornam outras funções
"""

def ola(msg, nome):
    def saudar():
        return f'{msg}, {nome}!'
    return saudar

one = ola("Bom dia", "Lucas")
two = ola("Boa noite", "Lucas")
print(one) #quando sem paretenses, ele mostra aonde está alocada na memoria a execução
print(two) #do codigo, porem ele não executa.
print(one()) #quando chamo parenteses "a função" ele busca na memoria e tras o resultado.
print(two())


print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')

def ola(msg):
    def saudar(nome):
        return f'{msg}, {nome}!'
    return saudar

one = ola("Bom dia")
two = ola("Boa noite")
print(one) #quando sem paretenses, ele mostra aonde está alocada na memoria a execução
print(two) #do codigo, porem ele não executa.
print(one('Lucas')) #quando chamo parenteses "a função" ele busca na memoria e tras o resultado.
print(two('Lucas'))