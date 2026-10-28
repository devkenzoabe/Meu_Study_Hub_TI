"""Desenvolva o programa que leia vários números digitados pelo usuário
e use o valor -1 como condição (flag) de saída da estrutura de repetição.
Na tela de saída, mostre a quantidade de números digitados.
Analise o problema e verifique quais são os dados que o usuário precisa
fornecer (digitar) como entrada.
"""

lista = []

print('\nDigite [-1] par sair!')

while True:
    valor = int(input('\nDigite um número inteiro: '))
    if valor == -1:
        break

    lista.append(valor)

qtd = len(lista)

print(f'\nQuantidade de números digitados: {qtd}')