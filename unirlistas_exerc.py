# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
l1=['Salvador', 'Ubatuba', 'Belo Horizonte']
l2=['BA', 'SP', 'MG', 'RJ']
# def zipper(lista1,lista2):
#     intervalo = min (len(lista1),len(lista2))
#     return[(lista1[i],lista2[i]) for i in range(intervalo)]
# print(zipper(l1,l2))


#outro modo de fazer pegando a menor lista

# print(list(zip(l1,l2)))


# outro modo pegando a maior lista

from itertools import zip_longest

print(list(zip_longest(l1,l2,fillvalue='Sem cidade')))