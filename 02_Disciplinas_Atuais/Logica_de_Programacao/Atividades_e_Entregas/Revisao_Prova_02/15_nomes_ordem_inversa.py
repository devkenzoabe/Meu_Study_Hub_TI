# Peça 5 nomes, guarde-os em uma lista e mostre os nomes na ordem inversa à que foram digitados.
lista = []

for name in range(0, 5):
    nome = input('Digite um nome: ')
    lista.append(nome)

lista.reverse()
print(f'\nLista com os nomes na ordem inversa: {lista}')