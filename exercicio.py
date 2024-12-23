nome =input('Qual seu nome ?')
idade = input('Qual sua idade ?')
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome de tras pra frente é {nome[::-1]}')
    
    if ' 'in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é :{nome[0]}')
    print(f'a ultima letra do seu nome é :',nome[-1])

