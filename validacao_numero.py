def valida_int(msg_num):
	"""
	Solicita um número inteiro positivo ao usuário.
	Continua pedindo até receber um valor válido.
	"""
	while True:
		try:
			num = int(input(msg_num))
			if num < 0:
				print('Digite um número positivo!\n')
			else:
				return num
		except ValueError:
			print('Digite apenas números!\n')

# Programa principal

num = valida_int('Digite um número: ')
print(f'Número digitado: {num}.')