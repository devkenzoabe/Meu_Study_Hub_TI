ct_masc = 0
ct_fem = 0
maior_altura = float('-inf')
menor_altura = float('inf')
soma_alturas = 0

print('\nDigite [0] para sair')

while True:
    altura = float(input('\nDigite a altura: '))
    if altura == 0:
        break
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

    soma_alturas += altura

    genero = str(input('\nDigite [m] para masculino:\nDigite [f] para feminino\nOpção: '))
    if genero == 'm':
        ct_masc += 1
    elif genero == 'f':
        ct_fem += 1
    else:
        print('Você digitou uma opção inválida!')

media_alturas = soma_alturas / (ct_masc + ct_fem)

print(f'\nMaior altura: {maior_altura:.2f}')
print(f'\nMenor altura: {menor_altura:.2f}')
print(f'\nQuantidade de homens: {ct_masc}')
print(f'\nQuatidade de mulheres: {ct_fem}')
print(f'\nMédia das alturas: {media_alturas:.2f}')