# Crie uma função que receba três notas e retorne a média. Na função principal, mostre 
# a média e informe se o aluno foi  aprovado, considerando média maior ou igual a 6.
def media_notas(a, b, c):
    return (a + b + c) / 3

def main():
    nota1 = float(input('\nDigite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))

    resultado_media = media_notas(nota1, nota2, nota3)
    print(f'\nMédia do aluno: {resultado_media:.2f}')

    if resultado_media >= 6:
        print('O aluno foi Aprovado!')
    else:
        print('O aluno foi Reprovado!')

if __name__ == '__main__':
    main()