string = 'ABCDE' #5 caracteres
lista = [123, True, "Lucas de Araujo", 2.4]
print(lista, type(lista))
#acessar um elementro por indice
print(lista[2].upper() , type(lista[2]))

num_lista = [1, 2, 3, 4]
num_lista[1] = 2000
print(num_lista)
del num_lista[1]
print(num_lista)

num_lista.append(50) #adicionando o 50 ao final da lista
print(num_lista)
num_lista.pop() #remove o ultimo item da lista. nesse caso o 50.

num_lista.insert(0,20) # em qual indice, qual valor deseja adicionar a lista
print(num_lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
lista_a.extend(lista_b)
print(lista_a)

lista_d = lista_a.copy()