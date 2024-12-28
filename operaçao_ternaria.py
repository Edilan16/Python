"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)   1 forma de fazer
# digito = 9  # > 9 = 0
# novo_digito = digito if digito <= 9 else 0   2 forma de fazer
# novo_digito = 0 if digito > 9 else digito    3 forma de fazer
# print(novo_digito)
print('Valor' if False else 'Outro valor' if False else 'Fim')# 4 forma 