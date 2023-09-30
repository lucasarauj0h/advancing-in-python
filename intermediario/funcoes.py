"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
Refatorar = editar o código.
"""

def soma(x,y, z):
    print(f'x = {x}; y = {y}; z = {z};  soma = {x+y+z}')

soma(1, 5, 4)
soma(4, y=5, z=4) #A partir do momento que eu nomeio um argumento, tenho q nomear os proximos

#o que acontece caso eu tenha uma funcao com 2 parametro, e agor ele passa a receber 3?

def sum(x,y,z=None): #solução -> atribuir o valor 0 para z ou como None
    # def sum(x,y,z=0):    
    # caso eu faça def sum(x,y= None, z), todos os valores depois de y também
    # terão que vir com valores atribuidos.
    if z is None:
        print(f'{x= } {y= } sum =', x+y)
    else:
        print(f'{x= } {y= } {z= } sum =', x+y+z)

    

sum(1, 2, 0)
sum(20,40, 0)
sum(1111,4444)