# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo


# alias 1 - import nome_modulo as apelido
# alias 2 - from nome_modulo import objeto as apelido
# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

import sys

print(sys.platform)

from sys import exit, platform 

print(platform) #quando usado o from, eu não preciso usar sys.platform. 

import sys
sys = 'var' #caso eu transforme meu import em variavel, ele vira uma str e perde seus
#atributos de módulos.
# print(sys.platform)
import sys as s #estou apelidando sys de s

print(s.platform)

from sys import platform as pf
print(pf)