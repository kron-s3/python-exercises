def verificar_dado(lista, dado):
    for i in range(len(lista)):
        if lista[i] == dado:
            return i
    return -1

# Programa principal
numeros = [8, 4, 6, 0]

print(verificar_dado(numeros, 8))
