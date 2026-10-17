import math

print('Vamos calcular o volume de uma esfera! ')

raio = float(input('\nQual o valor do raio: '))
volume = (4 * math.pi * raio ** 3) / 3

print(f'\nVolume da esfera: {volume:.2f}')