import statistics

# 1 - Aplicar a média
print(statistics.mean([7,8,9,6,4,8])) #passase uma lista como parametro, mean - média

# 2 - Aplicar a mediana
print(statistics.median([1, 3, 4, 5, 5 ,3 , 6, 7])) #passa-se uma lista c/ 
#argumento e retorna-se a mediana da lista

# 3 - Aplicar a moda (mais repetido)
print(statistics.mode([4,4,846,8,44,1,25,4,7,3,4,8,7,3,4,7]))

# 4 - Desvio padrão 
print(statistics.stdev([4,4,3,4,6,3,4,2,3,4,6,7,3,4,5]))
