import sys

iterable = ['Eu', 'Tenho', "__iter__"]
iterator = iterable.__iter__()# tem __iter__ e __next__
#unica responsabilidade do iterator é te entregar um valor por vez
#n sabe qm é o primeiro, anterior, ultimo, tamanho, só sabe entregar o proximo
print(next(iterator))
#generator são "funções que sabem pausar."
lista = [n for n in range(10000)] # <- isso oculpa muito espaço na memoria
#e em casos de projetos enormes, seria um problema na eficiencia do algoritmo
#portanto, usamos um generator e ele nos aponta para a memoria
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
#isso nos mostra a diferença de armazenamento de memoria entre uma lista e um generator
#o generator só entrega um valor por vez 

for i in generator:
    print(i)