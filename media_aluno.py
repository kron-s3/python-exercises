def calcular_media(soma, qtd):
	"""
	Calcula a divisão entre soma e qtd.
	Retorna o resultado dessa divisão.
	"""
	return soma / qtd
	
def validar_nome(msg_nome):
	"""
	Solicita um nome válido ao usuário.
	Continua solicitado até ele digitar um valor válido.
	"""
	while True:
		nome = input(msg_nome)
		if nome == '':
			print('Nome inválido.\n')
		else:
			return nome
			
def validar_nota(msg_nota):
	"""
	Solicita uma nota válida ao usuário. 
	Continua solicitado até ele digitar um valor válido.
	"""
	while True:
		try: 
			valor= float(input(msg_nota))
		except ValueError:
			print('Digite apenas números!\n')
		else:
			return valor

# Progama principal
print('Digite um número negativo para encerrar o programa.\n')
notas = []
nome = validar_nome('Digite o nome do aluno: ')

while True:
	nota = validar_nota(f'Digite a nota de {nome}: ')
	if nota >= 0:
		notas.append(nota)
	else:
		break

contador = 0
soma = 0

for nota in notas:
	contador += 1
	soma += nota

if contador == 0:
	print('Nenhuma nota foi digitada!')
else:
	media = calcular_media(soma, contador)
	print(f'\nMédia: {media:.2f}')