condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')

else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('passou no if')