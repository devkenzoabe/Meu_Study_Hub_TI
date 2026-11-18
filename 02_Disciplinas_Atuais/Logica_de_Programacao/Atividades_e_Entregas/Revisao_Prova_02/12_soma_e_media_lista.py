# Leia 8 números, guarde-os em uma lista e mostre a soma e a média deles.
lista = []

for i in range(0, 8):
    numero = float(input('Digite um número: '))
    lista.append(numero)

print(f'\nLista: {lista}')
print(f'Soma dos números da lista: {sum(lista)}')
print(f'Média da lista: {sum(lista) / len(lista):.2f}')