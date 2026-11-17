#Cria a matriz
matriz = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

soma_matriz = 0
ct_matriz = 0
valores_maior_20 = 0

#Preenche a matriz
for l in range(0, 1+1):
    for c in range(0, 4+1):
        matriz[l][c] = int(input(f'Digite um valor para a matriz: '))
        soma_matriz += matriz[l][c]
        ct_matriz += 1
        if matriz[l][c] > 20:
            valores_maior_20 += 1

#Imprime a matriz
for l in range(0, 1+1):
    print('[', end='')
    for c in range(0, 4+1):
        print(f'{matriz[l][c]:^5}', end='')
    print(']')

media_matriz = (soma_matriz / ct_matriz)

#Imprime a matriz calculada
print(f'Soma da matriz: {soma_matriz:.2f}')
print(f'Média da matriz: {media_matriz:.2f}')
print(f'Valores maior 20: {valores_maior_20}')

#Inserindo o valor 111 na linha 1 coluna 3 da matriz
matriz[1][3] = 111

#Imprimindo a matriz com o novo valor 111
print(f'Colocando 111 na linha 1 coluna 3: {matriz[1][3]}')
