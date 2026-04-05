def verificar_dado(lista, dado):
    contador = -1
    if dado in lista:
        contador += 1
        print('Dado encontrado!')
        return f'Índice: {contador}.'
    else:
        return -1

# Programa principal

numeros = [8, 4, 6, 0]

print(verificar_dado(numeros, 8))