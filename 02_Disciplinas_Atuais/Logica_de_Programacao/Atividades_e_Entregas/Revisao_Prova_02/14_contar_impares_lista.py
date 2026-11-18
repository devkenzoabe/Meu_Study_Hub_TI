# Leia 6 números, guarde-os em uma lista e mostre somente os ímpares.
lista = []

for i in range(0, 6):
    numero = int(input('\nDigite um número: '))
    lista.append(numero)

print('\nNúmeros ímpares na lista:')
for num in lista:
    if num % 2 != 0:
        print(num)