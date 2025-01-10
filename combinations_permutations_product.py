# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations,permutations,product

def print_iter(iterador):
    print(*list(iterador),sep='\n')
    print()
    
    
pessoas=[
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta','branca'],
    ['P','M','G'],
    ['Masculino','Feminino','Unisex'],
    ['algodão','poliester'],
    
]
print('Combinations')
print_iter(combinations(pessoas,2))
print('permutations')
print_iter(permutations(pessoas,2))
print('product')
print_iter(product(*camisetas))
