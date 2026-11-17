def positivo_nulo_negativo(numero):
    if numero == 0:
        print(f'\nValor nulo: {numero:.2f}')
    elif numero > 0:
        print(f'\nValor positivo: {numero:.2f}')
    else:
        print(f'\nValor negativo: {numero:.2f}')

def main():
        positivo_nulo_negativo(float(input('\nDigite um número: ')))


if __name__ == '__main__':
    for i in range(1, 3):
        main()