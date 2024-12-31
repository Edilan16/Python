def criar_saudacao(saudacao,nome):
    def saudar(nome):
        return f'{saudacao},{nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia','Luiz')
falar_boa_noite = criar_saudacao('boa Noite','Luiz')

# print(falar_bom_dia())
# print(falar_boa_noite())

for nome in ['Rebeca','Edilan','Léia']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))