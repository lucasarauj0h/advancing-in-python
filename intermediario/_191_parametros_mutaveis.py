def new_client(name, lista=[]):
    lista.append(name)
    return lista

clients= new_client('Lucas')
new_client('Joana', clients)
print(clients)

clients2 = new_client('Jorge')
new_client('Amadeu', clients)
print(clients2) 

# o problema é que, uma vez que eu não passe o parametro, ele vai adicionar esse parametro
# a lista presente na primeira chamada da função

print('-'*100)
print('Problema resolvido:')
print('-'*100)

def new_client(name, lista=None):
    if lista is None:
        lista=[]
    lista.append(name)
    return lista

clients= new_client('Lucas')
new_client('Joana', clients)
print(clients)

clients2 = new_client('Jorge')
new_client('Amadeu', clients2)
print(clients2) 
#dessa maneira, caso a função não receba argumento, ela criara uma nova lista dentro
#da funcao e retornara essa lista do 0, atribuida a uma variavel

#com parametro mutavel, o parametro vai ser sempre o mesmo todas as vezes que for chamado