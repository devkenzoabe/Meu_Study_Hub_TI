#Cria a matriz
matriz = [ 
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

#Cria variáveis
ct_matriz = 0

#Preenche a matriz
for l in range(0, 2+1):
    for c in range(0, 4+1):
        matriz[l][c] = float(input(f'Digite um valor para a matriz: '))
        ct_matriz += 1

# 1.	Exibição na vertical: mostrar todos os valores da matriz, um abaixo do outro, indicando a posição de cada elemento (linha e coluna).
print('\nMatriz na vertical:')

for l in range(0, 2+1):
    for c in range(0, 4+1):
        print(f'Valor: {matriz[l][c]} | Linha: {l} | Coluna: {c}')

# 2.	Exibição na horizontal: mostrar os valores da matriz em uma única sequência, linha por linha.
print('\nMatriz na horizontal:')

for l in range(0, 2+1):
    for c in range(0, 4+1):
        print(f'{matriz[l][c]}', end=' ')
print()

# 3.	Exibição em formato de tabela: mostrar os valores organizados em linhas e colunas, respeitando a estrutura original da matriz.
print('\nMatriz em formato de tabela:')

for l in range(0, 2+1):
    print('[', end='')
    for c in range(0, 4+1):
        print(f'{matriz[l][c]:^5}', end='')
    print(']')

# 4.	Soma dos valores: calcular e mostrar a soma de todos os elementos armazenados na matriz.
soma_matriz = 0

for l in range(0, 2+1):
    for c in range(0, 4+1):
        soma_matriz += matriz[l][c]

print(f'\nSoma da matriz: {soma_matriz}')             

# 5.	Média dos valores: calcular e mostrar a média aritmética dos 15 elementos.
media_matriz = soma_matriz / ct_matriz
print(f'\nMédia da matriz: {media_matriz:.2f}')

# 6.	Maior valor: identificar e mostrar o maior número armazenado na matriz.
maior_numero = float('-inf')

for l in range(0, 2+1):
    for c in range(0, 4+1):
        if matriz[l][c] > maior_numero:
            maior_numero = matriz[l][c]

print(f'\nMaior número da matriz: {maior_numero}')     

# 7.	Menor valor: identificar e mostrar o menor número armazenado na matriz.
menor_numero = float('inf')

for l in range(0, 2+1):
    for c in range(0, 4+1):
        if matriz[l][c] < menor_numero:
            menor_numero = matriz[l][c]

print(f'\nMenor número da matriz: {menor_numero}')    

# 8.	Contagem: calcular e mostrar quantos elementos da matriz possuem valores maiores que 10.
numeros_maior_10 = 0

for l in matriz:
    for valor in l:
        if valor > 10:
            numeros_maior_10 += 1

print(f'\nValores da matriz maiores que 10: {numeros_maior_10}')