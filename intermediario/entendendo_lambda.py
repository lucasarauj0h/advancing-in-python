def executa(funcao, *args):
    return funcao(*args) #retorna uma funcao com os argumentos passados

def soma(x,y):
    return x+y

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero*multiplicador
    return multiplica

duplica = criar_multiplicador(2) #como eu faria isso em lambda?
print(duplica(5))
duplica = executa(
    lambda mult: lambda num: num*mult , 2 #lambda [var]: [return], [*argumentos]
    #nesse caso, lambda mult: return (funcão num, essa função num retorna num*mult)
    #por fim passo os argumentos da função mult, e o num fica pendente.
)
print(duplica(66))

print(
    executa( 
        lambda x,y: x+y, 2, 3 #estou passando como parametro uma funcao, com argumentos 
    ),
    executa(soma, 2, 3) #passei uma funcao, e ao lado os argumentos.
)

print(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5,6,7
    )
)