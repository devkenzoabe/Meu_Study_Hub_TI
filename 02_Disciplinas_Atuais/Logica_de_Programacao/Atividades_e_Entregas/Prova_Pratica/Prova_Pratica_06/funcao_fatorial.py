def fatorial(n):
    if n == 0 or n == 1:
        return 1

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado


def main():
    numero = int(input('\nEscolha um número: '))
    resultado_fatorial = fatorial(numero)
    print(f'O fatorial de {numero} é {resultado_fatorial}')


if __name__ == '__main__':
    main()