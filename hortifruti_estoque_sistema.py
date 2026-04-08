estoque = {}

produto = input('Informe o nome do produto: ')
quantidade = int(input('Informe a quantidade de produto: '))

if produto in estoque:
    estoque[produto] += quantidade
else:
    estoque[produto] = quantidade

print(estoque)