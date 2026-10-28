ct_valores = 0
soma_valores = 0
menor_valor = float('inf')
maior_valor = float('-inf')
valores50 = 0

print('\nDigite [-1] para sair')

while True:
    valor = float(input('\nDigite um valor: '))

    if valor == -1:
        break
    if valor > maior_valor:
        maior_valor = valor
    if valor < menor_valor:
        menor_valor = valor
    if valor >= 50:
        valores50 +=1

    ct_valores += 1
    soma_valores += valor

if ct_valores == 0:
    print('\nNão é possível divirdir por 0!')
else:
    media_valores = soma_valores / ct_valores
    print(f'\nQuantidade de valores: {ct_valores}')
    print(f'Soma dos valores: {soma_valores}')
    print(f'Média Aritmética: {media_valores}')
    print(f'Maior valor: {maior_valor}')
    print(f'Menor valor: {menor_valor}')
    print(f'Quantidade de valores maior ou igual a 50: {valores50}')