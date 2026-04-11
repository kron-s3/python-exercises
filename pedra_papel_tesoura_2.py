def validar_escolha(msg_escolha):
    while True:
        try:
            escolha = int(input(msg_escolha))
        except ValueError:
            print('Valor inválido!\n')
        else:
            return escolha

# Programa principal
import random

resultados = []

jogadas = {
    1: 'Pedra',
    2: 'Papel',
    3: 'Tesoura'
}

regras = {
    1: 3,
    2: 1,
    3: 2,
}
while True:
    jogador = validar_escolha('Escolha sua jogada: ')
    if jogador == 0:
        print('Encerrando...\n')
        break
    if jogador not in jogadas:
        print('Escolha inválida!\n')
        continue

    jogada_jogador = jogadas[jogador]

    computador = random.randint(1, 3)

    jogada_computador = jogadas[computador]

    print(f'Jogador: {jogada_jogador}')
    print(f'Computador: {jogada_computador}\n')

    if jogador == computador:
        resultado = 'Empate!'
    elif regras[jogador] == computador:
        resultado = 'Jogador ganhou!'
    else:
        resultado = 'Computador ganhou!'

    print(resultado)
    print(' ')

    resultados.append(resultado)

jogador_vitorias = resultados.count('Jogador ganhou!')
computador_vitorias = resultados.count('Computador ganhou!')

print('--- RESULTADO FINAL ---')
if jogador_vitorias == computador_vitorias:
    print('Deu empate!')
elif jogador_vitorias > computador_vitorias:
    print('Jogador venceu o jogo!')
else:
    print('Computador venceu o jogo!')
