def validar_texto(msg_texto):
    while True:
        texto = input(msg_texto).strip()
        if texto == '':
            print('Valor inválido!')
        else:
            return texto

def validar_numero(msg_numero):
    while True:
        try:
            numero = int(input(msg_numero))
        except ValueError:
            print('Valor inválido!')
        else:
            return numero

# Programa principal
from datetime import datetime

pessoas = {
    'nome': [],
    'ano_nasc': [],
    'sexo': []
}

while True:
    nome = validar_texto('Nome: ')
    if nome.lower() == 'sair':
        break
    else:
        ano_nascimento = validar_numero('Ano de nascimento: ')
        sexo = validar_texto('Sexo: ').lower()

        print(' ')

        pessoas['nome'].append(nome)
        pessoas['ano_nasc'].append(ano_nascimento)
        pessoas['sexo'].append(sexo)

ano_atual = datetime.now().year
soma = 0
for ano in pessoas['ano_nasc']:
    idade = ano_atual - ano
    soma += idade

mulheres_menos_30 = []
homens_acima_media = []

if len(pessoas['ano_nasc']) > 0:
    media = soma / len(pessoas['ano_nasc'])
    print(f'\nQtd de pessoas cadastradas: {len(pessoas["nome"])}')
    print(f'Média das idades: {media}')
    for i in range(len(pessoas['nome'])):
        idade = ano_atual - pessoas['ano_nasc'][i]
        sexo = pessoas['sexo'][i]
        if sexo == 'feminino' and idade < 30:
            mulheres_menos_30.append(pessoas['nome'][i])

        if sexo == 'masculino' and idade > media:
            homens_acima_media.append(pessoas['nome'][i])

    print(f'Mulheres com menos de 30 anos: {mulheres_menos_30}.')
    print(f'Homens com idade acima da média: {homens_acima_media}.')
else:
    print('Nenhuma pessoa cadastrada.')