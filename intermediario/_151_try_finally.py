#try, finally
#
try:
    print('entrou no try')
    pritn(w22) # <------- erro
except:
    print('encontrou um erro') # <------ vai executar pq tem um erro acima
finally:
    print('sempre será executado, independente do erro.')