# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    multi = 1

    for i in args:
        multi *= i

    return multi

def paridade(x):
    if (int(x) % 2) == 0:
        print("par")
    else: 
        print("impar")

x = input("Digite um número inteiro qualquer: " )
paridade(x)


print(mult(2,2,2,2,2,2,2,2))
    