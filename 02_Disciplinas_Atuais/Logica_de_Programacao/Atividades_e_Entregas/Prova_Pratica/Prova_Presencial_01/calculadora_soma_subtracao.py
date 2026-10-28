numero1 = float(input('\nDigite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

print('\nEscolha a operação aritmética desejada:\n[1] - soma\n[2] - subtração')

operacao_desejada = int(input('Digite a operação desejada: '))

if operacao_desejada == 1:
    soma = numero1 + numero2
    print(f'\nValor da soma: {soma}')
elif operacao_desejada == 2:
    subtracao = numero1 - numero2
    print(f'\nValor da subtração: {subtracao}')
else:
    print('\nOperação Inválida!')

