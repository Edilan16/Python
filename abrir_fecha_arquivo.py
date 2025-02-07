# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
# Criando arquivos com Python + Context Manager with
# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
import os
caminho_arquivo = 'aula116.txt'
# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')
    
with open(caminho_arquivo,'w+',encoding='UTF-8')as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(('linha 3\n','linha 4\n'))
    arquivo.seek(0)
    print(arquivo.read())
    print('lendo')
    arquivo.seek(0)
    print(arquivo.readline(),end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    
    print('READLINES')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())
    
    print('#'*10)
    with open(caminho_arquivo, 'r')as arquivo:
        print(arquivo.read())
        
        
os.remove(caminho_arquivo)
os.rename('aula116-2.txt')