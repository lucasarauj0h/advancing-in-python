nomes = ['Lucas', 'Diana', 'Maria'] 
nomes.append('Cesar')
print(nomes)
lista_enumerada = enumerate(nomes)
print(lista_enumerada, nomes)
for i in lista_enumerada:
    print(i)

#o iterator só pode ser consumido uma vez (enumerate), caso eu tente denovo nao vai rolar
#pois ja foi consumido. 
for i in lista_enumerada:
    print(i)

#para contonar esse problema, devemos colocar o iterator diretamente no for in
print('novo iterator')
for i in enumerate(nomes):
    print(i)

new_case = list(enumerate(nomes))
print(new_case, type(new_case))


for i in new_case:
    a, b = i # a = indice/enumerator, b = nome 
    print(a,b)
print('#')
for num, name in new_case:
    print(num,name)