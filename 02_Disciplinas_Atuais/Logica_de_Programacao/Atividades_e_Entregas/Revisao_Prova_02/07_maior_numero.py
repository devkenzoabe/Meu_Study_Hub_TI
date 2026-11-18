# Crie uma função maior(a, b) que receba dois números e retorne o maior. Teste a função na parte principal do programa.
def maior(a, b):
    if a > b:
        return a
    else:
        return b

def main():
    valor1 = float(input('\nDigite um número: '))
    valor2 = float(input('Digite um número: '))
    maior_numero = maior(valor1, valor2)

    print(f'\nO maior número é: {maior_numero}!')

if __name__ == '__main__':
    main()