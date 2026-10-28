ct_bois = 0
soma_peso = 0

print('\nDigite 0 para sair!')

while True:
    peso_boi = int(input('\nDigite o peso do boi: '))

    if peso_boi == 0:
        break

    ct_bois += 1
    soma_peso += peso_boi

media_peso = soma_peso / ct_bois

print(f'\nQuantidade de bois: {ct_bois}')
print(f'Soma dos pesos: {soma_peso}')
print(f'Média dos pesos: {media_peso:.2f}')



