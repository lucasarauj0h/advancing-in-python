from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])

# for i in alunos_agrupados:
#     print(i)


# alunos = ['a', 'a', 'a', 'a', 'b', 'a', 'c', 'd']

grupos = groupby(alunos_agrupados, key=lambda a: a['nota'])
# print(*list(grupos), sep='\n')

for lista, group in grupos:
    print(lista)
    # print(group)
    print(list(group)) 

    # for aluno in group:
    #     print(aluno)


print()