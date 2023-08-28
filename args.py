"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


def soma(x, y):
    return x + y

def sum(*args):
    args = list(args)
    print(args, type(args))
    soma = 0
    for i in args:

        soma += i
    return soma

print(sum(1,2,3,4,5,65,76,7,7))

tupla = 1,2,3,4,5,65,76,7,7
# print(sum(tupla)) #dá erro pois, a funcao já transforma em uma tupla e passando
#o argumento desse jeito, continuaria em uma tupla, portanto ficaria uma tupla
#dentro de outra tupla (????). logo nos indica um erro

print(sum(*tupla)) #para resolvermos esse erro passamos com * (desempacota a tupla).
print(*tupla)