import os

lista=[]#lista vazia
while True:
    print('Selecione uma opção')
    letra_digitada=input('[i]inserir [a]apagar [l]listar [s]sair -> ')


    if letra_digitada == 'i':
        os.system('cls') # limpa terminal
        item = input('item: ')
        lista.append(item) 
        
        
        continue
    elif letra_digitada == 'a':
        os.system('cls') # limpa terminal
        for indice,nome in enumerate(lista):
            print(indice, nome)
        indice_str =  input('selecione um indice :')  
        try :  
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('por favor digite um numero inteiro')
        except IndexError:
            print('Esse indice não existe!')
    
    elif letra_digitada == 's':
        print('fim do programa')
        break
    elif letra_digitada == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Sua lista está vazia!')
        for indice,nome in enumerate(lista):
            print(indice, nome)
    else:
        print('Digite apenas [i] [a] [l]')