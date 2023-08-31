#try, except, else e finally


try:
    print('linha 1') #o codigo segue até o erro (linha 7)
    a = 18
    #b = 0 
    c = a/b
    print('linha 2') #como ocorreu um erro antes, essa linha não é executada
except ZeroDivisionError: #quando eu coloco o tipo de erro que eu quero que ele de uma 
    #caso o erro seja do tipo divisão por zero, ele ira executar esse bloco de except,
    #mas outros não. para outros erros ele irá apontar o erro. 
    ... #acabo de silenciar um erro
    print('tentou dividir por zero')
except NameError:
    print('variavel inexistente.')

print(':d')

#é possivel identificar erros no mesmo execpt

print()
print()
print()
print()


try:
    print('linha 1') #o codigo segue até o erro (linha 7)
    a = 18
    #b = 0 
    c = a/b
    print('linha 2') #como ocorreu um erro antes, essa linha não é executada
except (ZeroDivisionError, NameError) as error:
    print('dividiu por 0 ou nao definiu a variavel')
    print(error)