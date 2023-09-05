def decorador(func):
    print('entrou função decorador')
    def interna(*args):
        print('entrou função interna')
        for arg in args:
            is_num(arg)
        resultado = func(*args)
        return resultado
    return interna

@decorador
def soma(*args):
    total = 0
    for arg in args:
        total += arg
    return total


def is_num(*args):
    print('entrou função is_num')
    for arg in args:
        if not isinstance(arg, (float, int)):
            print('Não é numero')
            raise TypeError('Os parametro devem ser numeros')
        

multiplica = decorador(lambda x,y: x*y)
soma_cinco_dez = soma
print(soma_cinco_dez(41,7,7,77))
print(multiplica(4,8))