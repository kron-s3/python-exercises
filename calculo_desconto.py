cont = 1
total_produtos = 0
total_descontos = 0
qtd_produtos = int(input('Digite a quantidade de produtos em sua notinha: '))

while cont <= qtd_produtos:
	valor = float(input(f'Digite o valor do {cont}° produto: '))
	desconto = float(input(f'Digite o valor do desconto do {cont}° produto: '))
	
	while desconto >= valor:
		print('Desconto não pode ser maior que o valor do produto.')
		desconto = float(input('Digite o desconto novamente: '))
		
	cont = cont + 1
	total_produtos = total_produtos + valor
	total_descontos = total_descontos + desconto

print(' ')
print(f'Valor Total: R${total_produtos:.2f}')
print(f'Total em descontos: R${total_descontos:.2f}')	
print(f'Valor final: R${total_produtos - total_descontos:.2f}.')