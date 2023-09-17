caminho_arquivo = 'C:\\Users\\Lucas\\OneDrive\\Documentos\\avancandoPython'
caminho_arquivo += '\\aula186.txt'
# caminho_arquivo = 'test.txt'
# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

with open(caminho_arquivo, 'w+') as arquivo: #o uso do metodo W apaga tudo no arquivo e 
    print(type(arquivo)) #o cria novamente. 
    print("Olá mundo.")
    print('Arquivo vai ser fechado') #o arquivo começara a digitar na proxima linha
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n') #o arquivo ficará ao fim dessa linha
    arquivo.writelines(
        ('linha 3\n', '\n' ,'linha 5\n')
        )
    arquivo.seek(0,0) #voltando para o topo do arquivo
    print(arquivo.read())
    arquivo.seek(4,0)
    arquivo.write('Lendo\n')
    print(arquivo.readline())
    print('READLINES: ')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())

print("#"*40)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
    
with open(caminho_arquivo, 'a+') as arquivo: #o uso do metodo W apaga tudo no arquivo e 
    arquivo.write('linha 1 - a\n')
    arquivo.write('linha 2 - a\n')
    arquivo.seek(0,0) #voltando para o topo do arquivo
    print(arquivo.read())

import os

# os.remove(caminho_arquivo) #ou os.unlink
os.rename(caminho_arquivo, 'test_rename_186') #passando um caminho novo para o arquivo. 