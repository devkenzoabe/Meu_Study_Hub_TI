numeros_pares = 0
soma_pares = 0

print('\nDigite [0] para sair da repetição')

while True:
    numero = float(input('\nDigite um número: '))
    if numero == 0:
        break
    elif numero % 2 == 0:
        soma_pares += numero  # soma = soma + numero
        numeros_pares += 1  # ct = ct + 1

media_pares = soma_pares / numeros_pares

print('\nQuantidade de números pares:', numeros_pares)
print('\nMédia Aritmética dos números pares:', f'{media_pares:.2f}')