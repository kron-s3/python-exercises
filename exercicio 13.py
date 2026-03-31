def valida_idade(msg_idade):
    while True:
        try:
            idade = int(input(msg_idade))
            if idade > 0:
                return idade
            else:
                print('Idade deve ser maior do que zero.')
        except ValueError:
            print('Digite uma idade válida.')

# programa principal
nome = input('Nome: ')
idade = valida_idade('idade: ')

arquivo = open('cadastro simples.txt', 'a')
arquivo.write(f'{nome} - {idade}\n')
arquivo.close()

