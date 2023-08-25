while True:

    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador ( + - / * ) ")
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try: 
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except: 
        numeros_validos = None

    if numeros_validos is None:
        print("Algum número invalido.")
        continue
    
    operadores_valido = '+-/*'

    if operador not in operadores_valido:
        print("Operador invalido.")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    print("O resultado é: ")
    if operador == '+':
        soma = num_1_float + num_2_float
        print(num_1_float + num_2_float)
    elif operador == '-':
        sub = num_1_float - num_2_float
        print(num_1_float - num_2_float)
    elif operador ==  '/':
        div = num_1_float / num_2_float
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)


    sair = input('Quer sair? [s]im:   ').lower().startswith('s')
    #.lower() -> transforma tudo em minusculo
    #.startswith('s') -> "começa com: "('parametro'), se sim, retorna True, se não, False
    print(sair)
    if sair is True: 
        break 