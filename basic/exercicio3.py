nome = input("Digite seu nome: ")
i = 0
string = ""
while i < len(nome):
    if nome[i] != ' ':
        string = f'{string}*{nome[i]}'
    else:
        string = f'{string}* '
    print(string)
    i += 1