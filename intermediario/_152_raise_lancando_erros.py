print(123)
# raise ValueError("deu erro. (artificial)")
#porque é interessante? teste, caso eu queria comunicar que entrou em algo que nao deveria entrar

def deve_ser_num(*args):
    for i in args:
        print(i)
        if not isinstance(i, (float, int)):
            raise TypeError(
                f'{i} deve ser do tipo int ou float.'
            )
    return True

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError("Você está tentando dividir por 0")


def divide(n,d):
    # if d == 0:
    #     raise ZeroDivisionError("Você está tentando dividir por 0")
    deve_ser_num(n,d)
    nao_aceito_zero(d)
    return True

print(divide(4,'0'))    
