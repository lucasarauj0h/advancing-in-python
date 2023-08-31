print(__name__)

# import package #importei a pasta package
from package import modulo

print(modulo.soma(7,8))

from package.modulo import soma

print(soma(8,9))