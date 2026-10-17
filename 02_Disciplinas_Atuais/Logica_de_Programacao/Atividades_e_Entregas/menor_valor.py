menor_valor = float('inf') #menor_valor = 99999999
ct = 0
soma_valores = 0

while True:
    valor = int(input('\nDigite um número: '))
    if valor == 0:
        break
    if valor < menor_valor:
        menor_valor = valor
        ct += 1
        soma_valores += valor

media_valores = soma_valores / ct

print('\nO menor valor digitado foi:', menor_valor)
print('\nA média aritmética dos valores digitados foi:', f'{media_valores:.2f}')