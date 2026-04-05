def verificar_lista(lista, dado):
    indices = []
    for i in range(len(lista)):
        if lista[i] == dado:
            indices.append(lista[i])
            return indices
    return []

# Programa principal
numeros = [1, 2, 3, 8, 5, 9, 7, 8, 9, 10]
dados = 9

resultado = verificar_lista(numeros, dados)
print(resultado)