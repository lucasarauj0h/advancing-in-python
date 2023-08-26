lista = ['feijão', 'abacaxi', 'laranja', 'limão']

while True:
    enum_lista = list(enumerate(lista))
    print("Selecione uma opção: ")
    opcao = input("[i]nserir [a]pagar [l]istar   ")
    if opcao.startswith('i'):
        inserir = input("Qual item deseja adicionar?   ")
        lista.append(inserir)

    elif opcao.startswith('a'):
        for i, nome in enum_lista:
            print(i, nome)
        apagar = input("Qual item deseja apagar?   ")
        apagar = int(apagar)
        if apagar < len(lista):
            print(apagar)
            lista.pop(apagar)

        else:
            print('não é possivel apagar esse indice')

    elif opcao.startswith('l'):
        if len(lista) > 0:
            for i, nome in enum_lista:
                print(i, nome)
        else: 
            print('Lista vazia!')

    if opcao.startswith('s'):
        break