# Peça 5 números ao usuário, guarde-os em uma lista e depois mostre todos os números.
lista = []

for i in range(0, 5):
    numero = float(input('Digite um número: '))
    lista.append(numero)

print(f'Lista com os números do usuário: {lista}')