"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

def soma(l1, l2):
    lista_soma = list()
    minimo = min(len(lista_b),len(lista_a))
    for i in range(minimo):
        lista_soma.append(l1[i]+l2[i])
    return lista_soma

lista_somada = soma(lista_a ,lista_b)
print(lista_somada)
print(list(zip(lista_a,lista_b)))
lista_i = [x+y for x,y in zip(lista_a,lista_b)]
print(lista_i)

#class zip junta duas listas em tuplas, em caso de string ou soma em caso de numeors