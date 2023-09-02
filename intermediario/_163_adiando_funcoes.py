#adiando funções
def soma(x,y):
    return x+y

def multiplica(x,y):
    return x*y

def executa(funcao, x):
    def espera(y):
        return funcao(x, y)
    return espera

# def criar_multiplicador(multiplicador):
#     def multiplo(numero):
#         return multiplicador * numero
#     return multiplo d

soma_cinco = executa(soma,5)
multiplica_por_5 = executa(multiplica,5)
print(soma_cinco(5))
print(multiplica_por_5(10))
# print(soma_cinco(10))