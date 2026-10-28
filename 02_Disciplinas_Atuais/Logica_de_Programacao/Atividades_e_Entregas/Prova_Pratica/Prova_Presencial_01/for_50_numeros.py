ct_pares = 0
ct_impares = 0
soma_valores = 0

for i in range(0, 50, 1):
    valor = int(input(f'\nDigite o valor {i + 1}: '))

    if i % 2 == 0:
        ct_pares += 1
    else:
        ct_impares += 1

    soma_valores += valor

print(f'\nQuantidade de pares: {ct_pares}')
print(f'Quantidade de impares: {ct_impares}')
print(f'Soma dos valores: {soma_valores}')
