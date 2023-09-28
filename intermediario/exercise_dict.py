perguntas = [
    {
        'pergunta': 'quanto é 4+8? ',
        'opcoes': (4, 8, 12, 16),
        'resposta': 12,
    },   
    {
        'pergunta': 'quanto é 7*7? ',
        'opcoes': (49, 81, 21, 36),
        'resposta': 49,
    },   
    {
        'pergunta': 'em qual ano pedro alvarez cabral avistou as terras brasileiras?',
        'opcoes': (1488, 1888, 1500, 1612),
        'resposta': 1500,
    },   
    {
        'pergunta': 'quanto é 4*8? ',
        'opcoes': (40, 80, 32, 16),
        'resposta': 32,
    },
]

# for i in range(len(perguntas)):
#     print(perguntas[i])
#     #for questao, resp in perguntas[i].items():
#     p = perguntas[i].values()
#     print(perguntas[i].values())
#     print(p)

opcoes_perguntas = perguntas[0].get('opcoes')
acertos = 0

#print(perguntas[0])    
#print(perguntas[0].items())
#print(perguntas[0].get('pergunta'))

for i in range(len(perguntas)):
    #print(perguntas[i].items())
    print(perguntas[i].get('pergunta'))
    print('Escolha uma das opções abaixo: ')
    opcoes_perguntas = perguntas[i].get('opcoes')
    for p in range(len(opcoes_perguntas)):
        opcoes_perguntas = perguntas[i].get('opcoes')
        print(f'[{p}] - {opcoes_perguntas[p]}')

    correcao = int(input("Qual a opção correta?   "))
    try: 
        int(opcoes_perguntas[correcao])
        if int(opcoes_perguntas[correcao]) == int(perguntas[i].get('resposta')):
            print("Parábens, voce acertou!")
            acertos +=1
        else: print(f"Você errou, a resposta correta é {perguntas[i].get('resposta')}")
    except:
        print("Indice não existente, você errou a resposta.")

    print()
    print('--------------------------------------------------------')
    print()

print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')


# for i in perguntas[i].items():
#     print(perguntas[0].items())
#     print(perguntas[0].get('pergunta'))
#     print('Escolha uma das opções abaixo: ')
#     opcoes_perguntas = perguntas[0].get('opcoes')
#     for p in range(len(opcoes_perguntas)):
#         opcoes_perguntas = perguntas[0].get('opcoes')
#         print(f'[{p}] - {opcoes_perguntas[p]}')

#     correcao = int(input("Qual a opção correta?   "))
#     try: 
#         if int(opcoes_perguntas[correcao]) == int(perguntas[0].get('resposta')):
#             print("Parábens, voce acertou!")
#             acertos +=1
#         else: print(f"Você errou, a resposta correta é {perguntas[0].get('resposta')}")
#     except:
#         print("Indice não existente, você errou a resposta.")

