valor_inicial = int(input('\nDigite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))
valores = 0

if valor_inicial < valor_final:
    print(f'\nOrdem crescente de {valor_inicial} até {valor_final}:')
    for valor in range(valor_inicial, valor_final + 1, 1):
        print(valor)
        valores += 1
elif valor_inicial > valor_final:
    print(f'\nOrdem decrescente de {valor_inicial} até {valor_final}:')
    for valor in range(valor_inicial, valor_final - 1, -1):
        print(valor)
        valores += 1
else:
    print('\nOs valores são iguais!')
    valores = 1

print(f'\nTotal de valores: {valores}')