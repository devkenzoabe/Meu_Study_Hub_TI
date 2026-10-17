valor_a = float(input('Digite o valor de a:'))

if valor_a == 0:
    print('Não é possível realizar a ação. Dividr um número por 0 não é possível!')
else:
    valor_b = float(input('Digite o valor de b:'))
    raiz = -valor_b / valor_a
    print('Valor da raiz:', raiz)