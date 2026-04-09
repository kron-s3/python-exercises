cardapio = {
    'Lanche de Frango': 14,
    'Lanche de Atum': 18,
    'Croquete de Presunto e Queijo': 7.5,
    'Croquete de Carne': 7.5,
    'Pastel de Carne': 7,
    'Pastel de Queijo': 7,
}

print('-' * 15 + 'CARDÁPIO' + '-' * 15)
for chave, valor in cardapio.items():
    print(f'{chave} - R${valor:.2f}')

print('\nDigite sair para encerrar o programa.')

carrinho = {}

while True:
    produto = input('\nO que deseja comprar: ')
    if produto == 'sair' or produto == 'Sair':
        break
    elif produto not in cardapio:
        print('Ops! Não temos esse produto em nosso cardápio.')
        print('Tente novamente!')
        continue
    else:
        quantidade = int(input('Quantos produtos deseja comprar? '))
        while quantidade <= 0:
            print('Quantidade inválida!\n')
            quantidade = int(input('Quantos produtos deseja comprar? '))
        if quantidade > 0:
            if produto in carrinho:
                carrinho[produto] += quantidade
            else:
                carrinho[produto] = quantidade

print('\n--- Resumo da Compra ---')
total_geral = 0
for produto, quantidade in carrinho.items():
    total_produto = quantidade * cardapio[produto]
    total_geral += total_produto
    print(f'{quantidade}x {produto}: R${total_produto:.2f}')

if total_geral >= 100:
    valor_final = total_geral * 0.9
    print('Você obteve um desconto de 10%!')
elif total_geral >= 50:
    print('Você obteve um desconto de 5%!')
    valor_final = total_geral * 0.95
else:
    valor_final = total_geral

print(f'\nSubtotal: R${total_geral:.2f}')
print(f'Desconto: R${(total_geral - valor_final):.2f}')
print(f'Total final: R${valor_final:.2f}')