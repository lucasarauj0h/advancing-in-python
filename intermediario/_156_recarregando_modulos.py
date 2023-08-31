# o import é um singleton, ou seja, só pode existir
#uma instancia desse modulo, portanto
#o modulo só é importado uma vez,
#e não varias vezes.

# import _154_teste_main

# print(_154_teste_main.var)

for i in range(10):
    print(i)
    import _154_teste_main #não vai importar varias vezes, uma vez que foi
    #instanciado anteriormente 

print('fim laço for')

#se por um acaso eu queira recarregar esse modulo, eu uso uma outra biblioteca

import importlib

for i in range(10):
    print(i)
    importlib.reload(_154_teste_main) 
