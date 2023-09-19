# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

def clear():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

lista = []
desfazer = []
refazer = []
stop = True

while stop:

    print ("Comandos: listar; desfazer; refazer")
    x = str(input("Digite uma tarefa ou comando: "))
    
    if x == '0': 
        stop = False
        break
    
    clear()

    if x.lower() == 'desfazer':
        print(len(desfazer))
        if len(desfazer) < 1:
            print('Não há mais oque desfazer.')
        else: 
            refazer.append(lista.pop())
            print(refazer)
    elif x.lower() == 'refazer':
        if len(refazer) <= 0:
            print('Não há mais oque refazer.')
        else: 
            lista.append(refazer.pop())
            print(refazer)
    else: 
        lista.append(x)
   
    desfazer = lista
    print("items da lista: ")
    for i in range(len(lista)):
            print(lista[i])
