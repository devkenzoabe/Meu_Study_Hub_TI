quantidade_valores = 0
quantidade_valores_par = 0
quantidade_valores_impar = 0
soma_valores_par = 0
soma_valores_impar = 0

print('\nDigite [0] para sair')

while True:
    valor = float(input('\nDigite um valor: '))
    if valor == 0:
        break
    if valor % 2 == 0:
        quantidade_valores_par += 1
        soma_valores_par += valor
    if valor % 2 == 1:
        quantidade_valores_impar += 1
        soma_valores_impar += valor

    quantidade_valores += 1

media_par = soma_valores_par / quantidade_valores_par
media_impar = soma_valores_impar / quantidade_valores_impar
soma_valores = soma_valores_par + soma_valores_impar

print('\nMédia dos valores pares:', media_par)
print('Média dos valores ímpares:', media_impar)
print('Quantidade de valores:', quantidade_valores)
print('Soma dos valores:', soma_valores)