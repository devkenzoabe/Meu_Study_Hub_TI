numero_escolhido = int(input('\nDigite um número: '))
#ct_numero = 0

print(f'Ordem decrescente de {numero_escolhido} até 0:')

for i in range(numero_escolhido, -1, -1):
    print(i)
    #ct_numero += 1

print(f'Quantidade de valores: {numero_escolhido + 1}') #{ct_numero}