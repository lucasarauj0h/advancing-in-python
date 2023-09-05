palavras = ('pastel', 'sabonete', 'panela', 'piada', 'pernambuco',
            'cachorro', 'tabuada', 'paraguai', 'esquecido')
vogais = ('a','e','i','o','u')

for i in range(len(palavras)):
    print(f'Na palavra {palavras[i]}: temos: ', end='')
    for letras in palavras[i]:
        for indice in range(len(vogais)):
            if letras == vogais[indice]:
                print(f'{letras} ', end='')
    print() #fim