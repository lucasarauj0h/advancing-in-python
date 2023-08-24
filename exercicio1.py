"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('digite seu nome aq')
idade = input('agr sua idade')

if nome != 'null' or idade != 'null':
    print('seu nome é {nome}')
    print('seu nome invertido é {nome[::-1]}')
    print('a primeira letra do seu nome é {nome[0]}')
    print('a ultima letra do seu nome é {nome[:len(nome)]}')
else:
    print('desculpe, você deixou um dos campos vazio')
    