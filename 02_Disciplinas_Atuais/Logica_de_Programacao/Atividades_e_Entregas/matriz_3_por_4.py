#Cria a matriz 3x4
matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0,],
    [0, 0, 0, 0,],
]

#Preenchendo a matriz com input
for l in range(0, 2+1):
    for c in range(0, 3+1):
        matriz[l][c] = int(input(f'Digite um valor para a matriz: '))

#Mostra na horizontal
# for l in range(0, 2+1):
#     for c in range(0, 3+1):
#         print(f'{matriz[l][c]}', end='')

# #Mostra na vertical
# for l in range(0, 2+1):
#     for c in range(0, 3+1):
#         print(matriz[l][c])

#Imprimindo a matriz
for l in range(0, 2+1):
    print('[', end='')
    for c in range(0, 3+1):
        print(f'{matriz[l][c]:^4}', end='')
    print(']')

