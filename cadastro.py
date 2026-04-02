def menu():
	"""
	Exibe um menu ao usuário.
	"""
	print('\n--- MENU ---')
	print('1 - Cadastrar pessoa')
	print('2 - Listar pessoas')
	print('3 - Sair\n')

		
def validar_nome(msg_nome):
	"""
	Solicita ao usuário que digite um nome válido.

	:param msg_nome: Mensagem exibida ao usuário ao solicitar o nome.
	:return: Nome válido digitado pelo usuário.
	"""
	while True:
		nome = input(msg_nome)
		if nome == '':
			print('Nome inválido!\n')
		else:
			return nome
			
def validar_idade(msg_idade):
	"""
	Solicita ao usuário que digite uma idade válida.
	:param msg_idade: Mensagem exibida ao usuário ao solicitar a idade.
	:return: Idade válida digitado pelo usuário.
	"""
	while True:
		try:
			idade = int(input(msg_idade))
			if idade <= 0:
				print('Idade deve ser um número positivo e diferente de zero.\n')
			else: 
				return idade
		except ValueError:
			print('Digite apenas números!\n')
	
def validar_escolha(msg_escolha):
	"""
	Solicita que o usuário escolha uma opção do menu.
	:param msg_escolha: Mensagem exibida ao usuário ao solicitar a escolha dele.
	:return: Escolha válida escolhida pelo usuário.
	"""
	while True:
		try:
			escolha = int(input(msg_escolha))
			if escolha == 1 or escolha == 2 or escolha == 3:
				return escolha
			else:
				print('Opção inválida!\n')
		except ValueError:
			print('Digite apenas números!\n')

def arquivo_existe(nome_arquivo):
	"""
	Verifica se determinado arquivo existe.
	:param nome_arquivo: Nome do arquivo que deve ser verificado.
	:return: False se o arquivo não existir, True se o arquivo existir.
	"""
	try:
		arquivo = open(nome_arquivo, 'r')
	except FileNotFoundError:
		return False
	else:
		arquivo.close()
		return True
		
def salvar_dados(nome_arquivo, nome, idade):
	"""
	Salva os dados no arquivo.
	Cria arquivo caso ele não exista e salva os dados nele.
	:param nome_arquivo: Nome do arquivo onde deve ser salvado.
	:param nome: Nome válido digitado pelo usuário.
	:param idade: Idade válida digitada pelo usuário.
	:return:
	"""
	arquivo = open(nome_arquivo, 'a')
	arquivo.write(f'Nome: {nome}, idade: {idade}\n')
	arquivo.close()
	
def ler_dados(nome_arquivo):
	try:
		arquivo = open(nome_arquivo, 'r')
	except FileNotFoundError:
		return False
	else:
		print('--- Dados Cadastrados ---')
		dados = arquivo.read()

		if dados == '':
			print('Nenhum cadastro ainda.')
		else:
			print(dados)

		arquivo.close()
		return True

# Programa principal
while True:
	menu()
	
	nome_arquivo = 'cadastro.txt'
	escolha = validar_escolha('Escolha: ')

	print()
	
	if escolha == 1:
		nome = validar_nome('Digite o nome: ')
		idade = validar_idade('Digite a idade: ')
		existe = arquivo_existe(nome_arquivo)
		if existe:
			salvar_dados(nome_arquivo, nome, idade)
			print('Cadastro realizado com sucesso!')
		else:
			salvar_dados(nome_arquivo, nome, idade)
			print('Cadastro realizado com sucesso!')
	
	elif escolha == 2:
		if not ler_dados(nome_arquivo):
			print('Arquivo não encontrado!')
			print('Realize o primeiro cadastro para criar o arquivo!')

	elif escolha == 3:
		print('Encerrando...')
		break