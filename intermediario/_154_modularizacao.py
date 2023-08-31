# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import sys

import _154_teste_main #esse import é executado na hora em que é importado

print('este módulo se chama: ', __name__)
# print(*sys.path, sep='\n')
print(_154_teste_main.var)

from _154_teste_main import var as v
print(v)

sum = _154_teste_main.soma(7,8)
print(sum)