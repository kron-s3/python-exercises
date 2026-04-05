nome = input('Por favor, digite o seu nome: ')
while nome == '':
	nome = input('Por favor, digite o seu nome: ')
	continue
	
print(f'Olá {nome}, seja bem vindo-ao meu programa.')

print(' ')

print('CATEGORIAS')
print('1 - Supermercado')
print('2 - Refeições Fora')

print('')

categ = int(input('Qual categoria deseja analisar? '))

while categ != 1 and categ != 2:
	print('Categoria inválida, tente novamente.')
	print(' ')
	categ = int(input('Qual categoria deseja analisar?'))
	continue

if categ == 1:
	print('Você escolheu a categoria 1 - Supermercado.')
	
	print(' ')
	
	qtd = int(input('Quantos produtos serão analisados? '))
	
	print(' ')
	
	cont = 1
	valor_total = 0
	soma_desconto = 0
	
	while cont <= qtd:
		valor = float(input(f'Valor do {cont}° produto: R$'))
		desconto = float(input(f'Desconto no {cont}° produto: R$'))
		
		print(' ')
		
		cont += 1
		valor_total += valor
		soma_desconto += desconto
		valor_final = valor_total - soma_desconto
	
	print('Categoria: Supermercado')
	print(f'Valor total: R${valor_total:.2f}.')
	print(f'Total em descontos: R${soma_desconto:.2f}.')
	print(f'Valor final: R${valor_final:.2f}')
		
elif categ == 2:
	print('Você escolheu a categoria 2 - Refeições Fora.')
	
	print(' ')
	
	qtd = int(input('Quantos produtos serão analisados? '))
	
	print('')
	
	cont = 1
	valor_total = 0
	soma_desconto = 0
	
	while cont <= qtd:
		valor = float(input(f'Valor do {cont}° produto: R$'))
		desconto = float(input(f'Desconto no {cont}° produto: R$'))
		
		print(' ')
		cont += 1
		valor_total += valor
		soma_desconto += desconto
	
		valor_final = valor_total - soma_desconto
	
	print('Categoria: Refeições Fora.')
	print(f'Valor total: R${valor_total:.2f}.')
	print(f'Total em descontos: R${soma_desconto:.2f}.')
	print(f'Valor final: R${valor_final:.2f}')
