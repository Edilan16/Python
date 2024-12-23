numero = input('Vou dobrar o numero que você digitar: ')

numero_float = float(numero)
print(f'o dobro de {numero} é {numero_float * 2 } ')

try:
    numero = float(numero_float)
    print('FLOAT:',numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2}')

except:
    print('Isso não é um numero')