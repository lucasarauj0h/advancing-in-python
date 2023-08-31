#quando damos import em uma pasta, o arquivo __init__.py vem 
#automaticamente, sem precisar declarar 
# from package import modulo as _m

# from package import init, modulo as pg
# from package import modulo 

from package.modulo import soma as pm


print(pm(7,8))

# print(pg.init.dobra(7))
# print(_m.soma(2,3))