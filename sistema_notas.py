def validar_nota(msg_nota):
    """
    Solicita uma nota ao usuário e valida a entrada.

    A função garante que o valor digitado seja numérico e maior
    ou igual a zero.

    :param msg_nota: Mensagem exibida ao usuário.
    :return: Nota validada digitada pelo usuário.
    """
    while True:
        try:
            nota = float(input(msg_nota))
            if nota < 0:
                print('Valor inválido.\n')
            else:
                return nota
        except ValueError:
            print('Digite apenas números.\n')

def validar_nome(msg_nome):
    """
    Solicita um nome ao usuário e valida a entrada.

    A função garante que o nome não seja vazio.

    :param msg_nome: Mensagem exibida ao usuário.
    :return: Nome válido digitado pelo usuário.
    """
    while True:
        nome = input(msg_nome)
        if nome == '':
            print('Nome inválido.\n')
        else:
            return nome

def calcular_media(a, b, c):
    """
    Calcula a média aritmética de três valores.

    :param a: Primeira nota.
    :param b: Segunda nota.
    :param c: Terceira nota.
    :return: Média das três notas.
    """
    return (a + b + c) / 3

# Programa principal
nome_aluno = validar_nome('Nome do aluno: ')
nota1 = validar_nota('Nota 1: ')
nota2 = validar_nota('Nota 2: ')
nota3 = validar_nota('Nota 3: ')

print('')

media = calcular_media(nota1, nota2, nota3)
media_arredondada = round(media, 2)

if media_arredondada >= 7:
    situacao = 'Aprovado'
elif 5 <= media_arredondada < 7:
    situacao = 'Em exame.'
else:
    situacao = 'Reprovado'

dados = {
    'Nome do aluno': nome_aluno,
    'Média': media_arredondada,
    'Situação': situacao
}

for chave, valor in dados.items():
    print(f'{chave}: {valor}')