
import copy
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
novos_produtos =[
   {**produto,'preço':round(produto['preco']*1.1 )}
     
    for produto in copy.deepcopy( produtos)
]  
# print(*produtos, sep='\n')
# print()  
# print(*novos_produtos,sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'],
    reverse=True
)
# Ordene os produtos por preco crescente (do menor para maior)
# Gerexx   produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['preco']
)
# 
print(*produtos,sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome,sep='\n')
print()
print(*produtos_ordenados_por_preco,sep='\n')


pessoas=[
    {"nome":"ANA","idade":"19"},
    {'nome':'Julio','idade':'30'},
    {'nome':'Carlos','idade':'15'},
    {'nome':'Miguel','idade':'22'},
    {'nome':'Silas','idade':'14'}
      
]

def ordenar_por_idade(dicionarios , chave):
   return sorted (key=lambda pessoa: pessoa['idade'])
resultado = ordenar_por_idade(pessoas)
print(resultado)