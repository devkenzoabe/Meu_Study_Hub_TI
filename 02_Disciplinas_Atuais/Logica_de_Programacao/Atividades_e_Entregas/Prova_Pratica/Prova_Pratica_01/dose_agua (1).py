print('Vamos calcular a quantidade de água diária necessária para você!')

peso_usuario = float(input('\nDigite o seu peso em kg: '))
litros_necessarios = peso_usuario * 0.03

print(f'\nLitros necessários por dia: {litros_necessarios:.2f}L')