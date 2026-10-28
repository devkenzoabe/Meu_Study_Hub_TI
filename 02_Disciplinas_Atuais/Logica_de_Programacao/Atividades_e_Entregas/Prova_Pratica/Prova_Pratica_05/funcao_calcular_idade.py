def idade(ano_nascimento):
    return 2026 - ano_nascimento


def main():
    ano_nascimento = int(input('\nDigite o ano de nascimento:'))
    resultado = idade(ano_nascimento)
    print(f'\nResultado: {resultado}')


if __name__ == '__main__':
    main()