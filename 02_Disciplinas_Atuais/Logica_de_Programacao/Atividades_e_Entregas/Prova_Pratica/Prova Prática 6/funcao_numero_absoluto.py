def valor_absoluto(valor):
    if valor < 0:
        return valor * (-1)
    return valor


def main():
    numero = float(input('\nDigite um número: '))
    valor = valor_absoluto(numero)
    print(f'O valor absoluto de {numero} é {valor}!')

if __name__ == '__main__':
    main()
