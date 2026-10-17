def mostrar(mensagem, numero):
    print(mensagem)
    print(numero)


def main():
    mensagem = input('\nDigite algo: ')
    numero = int(input('Digite um número: '))
    mostrar(mensagem, numero)


if __name__ == '__main__':
    main()