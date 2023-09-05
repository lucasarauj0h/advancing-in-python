# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def unir_listas(l1, l2):
    lista_final = list()
    uniao = tuple()

    for i in range(len(l1)):
        uniao = (l1[i], l2[i])
        lista_final.append(uniao)
    return lista_final
        

cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']

uniao = unir_listas(cidade,estado)

print(uniao)

def zipper(l1,l2):
    i = min(len(l1),len(l2))
    return [
        (l1[i],l2[i]) for i in range(i)
    ]
print(zipper(cidade,estado))

print('ou -----')

print(zip(cidade,estado))
print(list(zip(cidade,estado)))
from itertools import zip_longest

print(list(zip_longest(cidade,estado)))

print(list(zip_longest(cidade,estado, fillvalue='SEM CIDADE')))
