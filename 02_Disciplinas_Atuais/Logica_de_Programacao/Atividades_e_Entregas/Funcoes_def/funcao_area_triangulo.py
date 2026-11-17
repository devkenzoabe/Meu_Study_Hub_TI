def area_triangulo(base, altura):
    return (base * altura) / 2


def main():
    base = float(input('\nDigite a base do triângulo: '))
    altura = float(input('Digite a altura do triângulo: '))
    print(f'Área do triângulo: {area_triangulo(base, altura)}')


if __name__ == "__main__":
    main()