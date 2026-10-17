def soma(a, b):
    return a + b


def subtrai(a, b):
    return a - b


def main():
    print('\nOperações:\n[+] - somar\n[-] - subtrai')
    operacao = str(input('Digite a Operação desejada: '))

    if operacao != '+' and operacao != '-':
        print('\nOperação Inválida!')
        return

    valor1 = int(input('\nDigite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))

    if operacao == '+':
        print(f'\nResultado da soma: {soma(valor1, valor2)}')
    else:
        print(f'\nResultado da subtração: {subtrai(valor1, valor2)}')


if __name__ == '__main__':
    main()