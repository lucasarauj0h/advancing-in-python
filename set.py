# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas

#sets são mutaveis mas só aceitam tipos imutaveis.
#tipos mutaveis - list, tupla, dict

s1 = set('Lucas')
s1 = {'Lucas', 1,2,3,4,3,3,33,3,3,3,1} #os sets eliminam naturalmente valores repetidos
tupla = (1,2,2,2,3,3,3,4,2,1,3,2,3,2,2,3,1)
s1 = set(tupla)
l2 = list(s1)
print(l2)
print(s1, type(s1))
print()
print(3 in s1) 
#verificando se existe um 3 no conjunto
#sets são eficientes para remover items duplicados

#set parecem dicionarios, mas n tem par de chaves, somente valor

#metodos uteis do set (add, update, clear, discard)

print()
print()

s1 = set()
s1.add('Lucas')
s1.add(1)
# s1.update('Lucas')
# s1.update(('Lucas A.',1,2,3))
# print(s1)
# s1.discard('Lucas A.')
# s1.discard('Lucas')
#s1.clear() #limpa todo o set (conjunto)
print(s1)

print()
print()

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas


s1 = {1, 2, 3, 4, 5, 6}
s2 = {3,4,5,6,7,8}
s3 = s1 | s2
print(s3, type(s3))
s3 = s1 & s2
print(s3, type(s3))
s3 = s1 - s2
print(s3, type(s3))
s3 = s1 ^ s2 #Itens que não estão em ambos, nesse caso, 1, 2, 7, 8
print(s3, type(s3))