brasileirao = ('Fortaleza', 'Athletico-PR', 'Atlético-GO', 'Bragantino',
                  'Bahia', 'Fluminense', 'Palmeiras', 'Flamengo', 'Atlético-MG',
                  'Corinthians', 'Ceará SC', 'Santos', 'Cuiabá', 'Sport Recife',
                  'São Paulo', 'Juventude', 'Internacional', 'Grêmio', 'América-MG',
                  'Chapecoense')
def primeiros():
    i=0
    #mostra os primeiros 5 colocados 
    while i < 5:
        print(f'{i+1}º - {brasileirao[i]}')
        i+=1 

def ultimos():
    i = 19
    while i > 15:
        print(f'{i+1}º - {brasileirao[i]}')
        i -= 1 

print('Primeiros colocados:')
primeiros()
print()

print('Ultimos colocados:')
ultimos()
time = 'Chapecoense'

def posicao(time):
    for i in brasileirao:
        if time.lower() == i.lower():
            print('121')
            print(f'O {time} {brasileirao.index(time)+1}º')

posicao(time)

def exibir(lista):
    for i in lista:
        print(i)

classificacao_ordenado = sorted(brasileirao)
print(brasileirao)
exibir(classificacao_ordenado)