print('Vamos fazer operações matemáticas:')

numero1 = float(input('\nDigite o primeiro número: '))
numero2 = float(input('\nDigite o segundo número: '))

print('\nEscolha a operação aritmética desejada:\n[1] - soma\n[2] - subtração\n[3] - multiplicação\n[4] - divisão')

operacao_escolhida = input('Digite a operação desejada: ')

if operacao_escolhida == '1':
    soma = numero1 + numero2
    print('\nValor da soma:', soma)
elif operacao_escolhida == '2':
    subtracao = numero1 - numero2
    print('\nValor da subtração:', subtracao)
elif operacao_escolhida == '3':
    multiplicacao = numero1 * numero2
    print('\nValor da multiplicação:', multiplicacao)
elif operacao_escolhida == '4':
    if numero2 == 0.0:
        print('Não é possível dividir por 0!')
    else:
        divisao = numero1 / numero2
        print('Valor da divisao:', divisao)
else:
    print('Operação inválida!')
