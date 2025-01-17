def validar_cpf(cpf):
    # Remove qualquer caracter não numérico
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os números são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Calculando o primeiro dígito verificador
    soma_1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito_1 = (soma_1 * 10) % 11
    if digito_1 == 10 or digito_1 == 11:
        digito_1 = 0

    # Calculando o segundo dígito verificador
    soma_2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito_2 = (soma_2 * 10) % 11
    if digito_2 == 10 or digito_2 == 11:
        digito_2 = 0

    # Verifica se os dígitos calculados são iguais aos fornecidos
    if int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2:
        return True
    return False

# Testando a função
cpf_input = input("Digite o CPF para validação: ")
if validar_cpf(cpf_input):
    print(f"O CPF {cpf_input} é válido.")
else:
    print(f"O CPF {cpf_input} é inválido.")
