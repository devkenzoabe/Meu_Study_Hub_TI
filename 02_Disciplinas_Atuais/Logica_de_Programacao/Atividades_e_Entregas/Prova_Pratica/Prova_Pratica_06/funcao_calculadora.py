def somar(a,b):
    resultado = a + b
    print(f'\n{a} + {b} = {resultado}')


def subtrair(a,b):
    resultado = a - b
    print(f'\n{a} - {b} = {resultado}')


def multiplicar(a,b):
    resultado = a * b
    print(f'\n{a} * {b} = {resultado}')


def dividir(a,b):
    resultado = a / b
    print(f'\n{a} / {b} = {resultado}')

def main():
    print('\nEscolha a operação desejada:')
    operacao = str(input('[+] - somar\n[-] - subtrair\n[*] - multiplicar\n[/] - dividir\nOperação escolhida: '))
    valor1 = int(input('\nInforme o primeiro valor: '))
    valor2 = int(input('Informe o segundo valor: '))

    if operacao == '+':
        somar(valor1,valor2)
    if operacao == '-':
        subtrair(valor1,valor2)
    if operacao == '*':
        multiplicar(valor1,valor2)
    if operacao == '/':
        dividir(valor1,valor2)


if __name__ == '__main__':
    main()