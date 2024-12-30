"""
Introduçao as funçoes(def) em python
Funções são trechos de codigos usados para
replicar determinada ação ao longo do seu codigo.
Elas podem receber valores para parãmetros (argumentos)
e retornar um valor especifico.
Por padrão, funçoes python retornam None (nada)
"""


def Print(a,b,c):
    print('Várias1')
    print('Várias1')
    print('Várias1')
    print('Várias1')

#------------------------------------

def imprimir (a,b,c):
    print(a,b,c)

imprimir(1,2,3) 
imprimir(4,5,6)  

#-------------------------------

def saudacao(nome='Sem Nome'):
    print(f'Olá,{nome}!')

saudacao('Edilan')
saudacao('Rebeca')
saudacao('Leia')
saudacao()

#--------------------

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)