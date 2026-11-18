# Peça 5 números ao usuário e conte quantos deles são pares.
numeros_pares = 0

for i in range(0, 5):
    numero_usuario = int(input('Digite um número: '))

    if numero_usuario % 2 == 0:
        numeros_pares += 1

print(f'\nQuantidade de números pares digitados: {numeros_pares}')