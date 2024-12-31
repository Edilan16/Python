# Manipulando chaves e valores em dicionários

pessoa ={}

##

chave = 'nome'

pessoa[chave] = 'Edilan Gomes'
pessoa['sobrenome'] = "Viana"

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))

if pessoa.get('sobrenome')is None:
    print('Não Existe')
else:
    print(pessoa['sobrenome'])
