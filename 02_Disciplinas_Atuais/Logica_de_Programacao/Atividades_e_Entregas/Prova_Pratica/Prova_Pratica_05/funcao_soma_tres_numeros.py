def somar(a, b, c):
    return a + b + c


def main():
    valor1 = int(input('\nDigite um valor: '))
    valor2 = int(input('Digite um valor: '))
    valor3 = int(input('Digite um valor: '))
    resultado = somar(valor1, valor2, valor3)
    print(f'\nResultado: {resultado}')


if __name__ == '__main__':
    main()