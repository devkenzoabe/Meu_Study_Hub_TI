# a. Crie uma lista vazia.
lista = []

# b. Leia vários números digitados pelo usuário e os armazene na lista. Use repetição.
print('\nDigite [-1] para sair!')

while True:
    numero = (float(input('\nDigite um número: ')))
    if numero == -1:
        break
    lista.append(numero)

# c. Mostre a lista na horizontal.
print(f'\nLista na horizontal: {lista}')

# d. Mostre a lista na vertical.
print(f'\nLista na Vertical:')

for numero in lista:
    print(numero)

# e. Mostre a quantidade de elementos armazenados na lista, não use variável contador.
qtd = len(lista)

print(f'\nQuantidade de números na lista: {qtd}')

# f. Mostre a soma dos valores da lista, não use variável somador.
soma_lista = sum(lista)

print(f'\nSoma dos números da lista: {soma_lista}')

# g. Mostre o maior valor da lista.
maior_numero = max(lista)

print(f'\nMaior número da lista: {maior_numero}')

# h. Mostre o menor valor da lista.
menor_numero = min(lista)

print(f'\nMenor número da lista: {menor_numero}')

# i. Faça uma pesquisa. Leia um valor digitado pelo usuário e verificar se ele está na lista.
# j. No item anterior, mostre também a posição (índice) do valor encontrado.
pesquisa = int(input('\nNúmero da pesquisa: '))

if pesquisa in lista:
    print(f'\nO número {pesquisa} está na lista e no indice {lista.index(pesquisa)}!')
else:
    print(f'\nO número {pesquisa} não está na lista.')

# k. Mostre a lista na ordem crescente.
lista.sort()
print(f'\nLista em ordem crescente: {lista}')

# l. Insira (acrescente) o valor 33 na posição (índice) 1 da lista.
lista.insert(1, 33)
print(f'\nAcrescentando 33 ao indice 1 na lista: {lista}')

# m. Mostre a lista na ordem decrescente.
lista.sort(reverse=True)
print(f'\nLista em ordem decrescente: {lista}')

# n. Calcule e mostre a média aritmética dos valores da lista.
# o. Mostre a média com três casas decimais.
media = sum(lista) / len(lista)
print(f'\nMédia da lista: {media:.3f}')

# p. Mostre a quantidade de valores maior que dez na lista.
numero_maior_10 = 0

for numero in lista:
    if numero > 10:
        numero_maior_10 += 1

print(f'\nQuantidade de número maior que 10: {numero_maior_10}')

# q. Porcentagem dos números maiores que dez da lista.
porcentagem_maior_10 = (numero_maior_10 / len(lista)) * 100

print(f'\nPorcentagem dos números maiores que 10: {porcentagem_maior_10:.2f}%')

# r. Remova o valor 33 da lista e depois mostre a lista.
lista.remove(33)
print(f'\nLista ao remover o número 33: {lista}')
