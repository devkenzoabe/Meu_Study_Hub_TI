def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def main():
    nota1 = float(input('\nDigite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))
    resultado_media = calcular_media(nota1, nota2)
    print(f'\nResultado da média: {resultado_media}')

