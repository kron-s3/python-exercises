def valida_float(msg_num):
	"""
	Valida a entrada do usuário, permitindo apenas números do tipo float.
	Continua solicitando até receber um número válido.
	
	"""
	while True:
		try:
			num = float(input(msg_num))
			return num
		except ValueError:
			print('Digite apenas números!\n')
	
def divisao(a, b):
	"""
	Calcula a divisão entre a e b.
	
	"""
	return a / b

# Programa principal
num1 = valida_float('Digite um número: ')
num2 = valida_float('Digite outro número: ')

print('')

try:
	resultado = divisao(num1, num2)
except ZeroDivisionError:
	print('Não é possível dividir por zero!\n')
else:
	print(f'{num1:.2f} / {num2:.2f} = {resultado}')
finally:
	print('Operação finalizada!')