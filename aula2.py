nome = 'Edilan'
altura = 1.68
peso = 77
imc= peso/(altura*altura)
print(nome,"tem:",altura,)
print('pesa',peso,'e seu IMC é ')
print(imc)
print('---------')
linha_1 = f'{nome} tem {altura:,.2f} de altura'
linha_2=f'pesa {peso} quilos e seu imc é:'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)