# Crie uma função que receba uma idade e informe se a pessoa é maior de idade. Na função principal, peça o nome e a idade e mostre uma mensagem para o usuário.
def verificar_idade(idade):
    if idade >= 18:
        return 'maior de idade!'
    else:
        return 'menor de idade!'

def main():
    nome = input('\nDigite o seu nome: ')
    idade_usuario = int(input('Digite a sua idade: '))

    print(f'\n{nome}, você é {verificar_idade(idade_usuario)}')

if __name__ == '__main__':
    main()