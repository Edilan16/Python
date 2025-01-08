numero = input('Vou dobrar o numero que você digitar: ')

numero_float = float(numero)
print(f'o dobro de {numero} é {numero_float * 2 } ')

try:
    numero = float(numero_float)
    print('FLOAT:',numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2}')

except:
    print('Isso não é um numero')
    
    
 # (Parte 2) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')