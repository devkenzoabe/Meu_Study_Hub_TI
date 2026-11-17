lista = []
print('\nDigite [0]para sair')

while True:
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break
    lista.append(valor)


print(f'\nValores da lista na horizontal: {lista}')
print(f'\nValores da lista na vertical:')

for valor in lista:
    print(valor)

qtd = len(lista)
soma_lista = sum(lista)
valor_maximo = max(lista)
valor_minimo = min(lista)

print(f'\nQuantidade de elementos na lista:{qtd}')
print(f'\nSoma dos elementos da lista: {soma_lista}')
print(f'\nMaior valor da lista: {valor_maximo}')
print(f'\nMenor valor da lista: {valor_minimo}')

pesquisa = int(input('\nValor da pesquisa: '))

if pesquisa in lista:
    print(f'\nO valor {pesquisa} está na lista!')
else:
    print(f'\nO valor {pesquisa} não está na lista!')

print(f'\nO valor {pesquisa} está no indice {lista.index(pesquisa)}!')

lista.sort()
print(f'\nLista em ordem crescente:\n{lista}')

lista.insert(1, 33)
print(f'\nAcrescentando 33 ao indice 1 na lista:\n{lista}')

lista.sort(reverse=True)
print(f'\nLista em ordem decrescente:\n{lista}')
