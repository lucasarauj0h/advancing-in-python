"""
Higher Order Functions
Funções de primeira classe
"""
def saudacoes(msg):
    return msg

def executa(funcao, texto): #funcao executa ta recebendo uma funcao como parametro
    return funcao(texto)

texto = executa(saudacoes,'Bom dia!')
print(texto)
    
def saudacoes_2(msg, nome):
    return f'{msg}, {nome}!'

def executa_2(funcao, *texto): #funcao executa ta recebendo uma funcao como parametro
    return funcao(*texto)

texto = executa_2(saudacoes_2,'Bom dia!', 'Lucas.')
print(texto)