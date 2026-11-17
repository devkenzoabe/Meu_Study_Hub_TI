menor_valor = float('inf') #menor_valor = 99999999
maior_valor = float('-inf') #maior_valor = -9999999
ct = 0

print('\nDigite [0] para sair da repetição')

while True:
    valor = int(input('\nDigite um valor: '))
    if valor == 0:
        break
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor
    ct += 1

print(f'\nO menor valor digitado foi: {menor_valor}')
print(f'\nO maior valor digitado foi: {maior_valor}')
print(f'\nA quantidade de valores digitados foi: {ct}')