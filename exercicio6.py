def valida_num(msg_num):
    while True:
        try:
            num = int(input(msg_num))
            if num >= 0:
                return num
            else:
                print('Não existe fatorial de números negativos.')
        except ValueError:
            print('Digite apenas números!')

def fatorial(num):
    fat = 1
    if num == 0:
        return fat
    elif num >= 1:
        for i in range(1, num + 1):
            fat *= i
        return fat

# programa principal
numero = valida_num('Digite um número: ')
resultado = fatorial(numero)
print(f'{numero}! = {resultado}')