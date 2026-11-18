# Peça um número ao usuário e mostre a tabuada dele de 1 a 10.
numero_escolhido = int(input('Digite um número: '))

print(f'\nTabuada do número {numero_escolhido}:')

for i in range(0, 11):
    print(f'{i} * {numero_escolhido} = {i * numero_escolhido}')