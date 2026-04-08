estoque = {
    'maçã': [1.20, 110],
    'abacaxi': [6.99, 240],
    'manga': [3.50, 123],
    'banana': [0.90, 570]
}

print('-' * 17 + 'Estoque' + '-' * 17)
for chave, valor in estoque.items():
    print(f'Produto: {chave} | Preço: R${valor[0]:.2f} | Qtd: {valor[1]}')

print('')

carrinho = {

}
while True:
    produto = input('Nome do produto: ')
    if produto == 'sair' or produto == 'Sair' or produto == 'SAIR':
        break
    elif produto not in estoque:
        print('Este produto não está disponível no estoque!\n')
        continue
    else:
        quantidade = int(input('Quantidade: '))
        quantidade_estoque = estoque[produto][1]
        if quantidade < 0:
            print('Quantidade inválida.\n')
            continue
        elif quantidade > quantidade_estoque:
            print('Quantidade indisponível.')
            continue
        else:
            if produto in carrinho:
                carrinho[produto] += quantidade
                print('Produto adicionado ao carrinho!\n')
            else:
                carrinho[produto] = quantidade
                print('Produto adicionado ao carrinho!\n')

total_geral = 0
for produto, quantidade in carrinho.items():
    total_produto = quantidade * estoque[produto][0]
    total_geral += total_produto
    estoque[produto][1] -= quantidade
    print(f'Produto: {produto} | Quantidade: {quantidade} | Total: R${total_produto:.2f}')

print('\nResumo da compra:')
print(f'Total geral: R${total_geral:.2f}')
print('\n' + '-' * 15 + ' Estoque Atualizado ' + '-' * 15)
for chave, valor in estoque.items():
    print(f'Produto: {chave} | Preço: R${valor[0]:.2f} | Qtd: {valor[1]}')

# Link: https://chatgpt.com/c/69d3d7e9-9ac4-832d-805e-b0bbd62c8ae8