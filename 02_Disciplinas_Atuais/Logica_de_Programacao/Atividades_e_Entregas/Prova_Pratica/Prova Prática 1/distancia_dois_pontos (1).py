import math

print('Vamos calcular a distância entre dois pontos quaisquer no plano cartesiano!')

x1 = float(input('Valor do x do ponto P: '))
y1 = float(input('Valor do y do ponto P: '))
print(f'P({x1:.2f}, {y1:.2f})')

x2 = float(input('\nValor do x do ponto Q: '))
y2 = float(input('Valor do y do ponto Q: '))
print(f'Q({x2:.2f}, {y2:.2f})')

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f'\nA distância entre os dois pontos é: {distancia:.2f}')