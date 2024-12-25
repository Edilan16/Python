"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria','Helena','Luiz']

for indice,valor in enumerate(lista):
    print(f"indice:{indice},Nome: {valor}")


"""
OUTRA FORMA DE RESOLVER
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))