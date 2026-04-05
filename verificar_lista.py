def verificar_lista(lista, dado):
    indices = []
    contador = 0
    for i in range(len(lista)):
        if lista[i] == dado:
            indices.append(i)
            contador += 1
    return indices, contador

# Programa principal
numeros = [1, 2, 3, 8, 5, 9, 7, 8, 9, 10]
dados = 9

resultado = verificar_lista(numeros, dados)
print(f'Índices: {resultado}')
