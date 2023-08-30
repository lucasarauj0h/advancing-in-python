#uma função que sabe pausar.
def generator (n=0):
    yield 1 # a função generator está pausada aqui.
    print("continuando")
    print("pós yield 1")
    yield 2 #segunda pausa
    print('vou acabar.!')
    yield 3 
    print('acabou')
    return 'acabou'

gen = generator(n=0)
print(gen) #a minha funcao generator está pausada, caso eu chame um next, ela
#vai mostrar o valor 1
print(next(gen)) #pausou no valor 1, nosso primeiro yield
print(next(gen)) #executou o codigo abaixo do 'yield 1' (primeira pausa) até o yield 2

for n in gen:
    print(n)

def gener (n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum: return 'acabou'

gen = gener()
for n in gen:
    print(n)