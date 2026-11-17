tabuada_escolhida = int(input('\nDigite a tabuada escolhida: '))

print(f'\nTabuada do número {tabuada_escolhida}:')

for i in range(0, 11):
    print(f'{i} * {tabuada_escolhida} = {i * tabuada_escolhida}')