# Leia 10 números, guarde-os em uma lista e mostre o maior e o menor valor.
lista = []

for i in range(0, 10):
    numero = float(input('Digite um número: '))
    lista.append(numero)

print(f'\nMaior número da lista: {max(lista)}')
print(f'Menor número da lista: {min(lista)}')