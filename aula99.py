from sys import path
import aula99_package.modulo
import aula99_package
from aula99_package import modulo
from aula99_package.modulo import *


print(soma_do_modulo(1,2))
print(aula99_package.modulo.soma_do_modulo(1,2))
print(modulo.soma_do_modulo(1,2))
print(variavel)
print(nova_variavel      )

# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
from aula99_package.modulo import fala_oi, soma_do_modulo
print(__name__)
fala_oi()