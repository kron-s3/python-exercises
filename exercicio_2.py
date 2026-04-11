import random

resultados = []

while True:
    jogador = int(input('Escolha sua jogada: '))
    if jogador == 0:
        print('Encerrando...\n')
        break
    elif jogador == 1:
        jogada_jogador = 'Pedra'
    elif jogador == 2:
        jogada_jogador = 'Papel'
    elif jogador == 3:
        jogada_jogador = 'Tesoura'
    else:
        print('Escolha inválida!\n')
        continue

    computador = random.randint(1, 3)
    if computador == 1:
        jogada_computador = 'Pedra'
    elif computador == 2:
        jogada_computador = 'Papel'
    else:
        jogada_computador = 'Tesoura'

    print(f'Jogador: {jogada_jogador}')
    print(f'Computador: {jogada_computador}\n')

    if jogador == computador:
        resultado = 'Empate!'
    elif jogador == 1 and computador == 3:
        resultado = 'Jogador ganhou!'
    elif jogador == 2 and computador == 1:
        resultado = 'Jogador ganhou!'
    elif jogador == 3 and computador == 2:
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