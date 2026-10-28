ct = 0
soma = 0
valores_maior_20 = 0

print('\nDigite [-1] para sair da repetição')

while True:
    numero = int(input('Digite um número: '))
    if numero == -1:
        break
    if numero > 20:
        valores_maior_20 += 1
    ct += 1
    soma += numero

if ct > 0:
    media_valores = soma / ct
    print('Média dos valores:', media_valores)
else:
    print('Não é possível dividir por 0')

print('Quantidade de número digitados:', ct)
print('Valor da soma:', soma)
print('Valores maior que 20:', valores_maior_20)