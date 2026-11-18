# Leia 5 notas e guarde-as em uma lista. Crie uma função que receba essa lista e retorne a média. 
# Mostre a média e informe se o aluno foi aprovado, considerando média maior ou igual a 6.
def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    lista = []

    for i in range(0, 5):
        nota = float(input(f'Digite a nota {i + 1}: '))
        lista.append(nota)

    media_notas = calcular_media(lista)
    print(f'Média do aluno: {media_notas:.2f}')

    if media_notas >= 6:
        print('O aluno foi Aprovado!')
    else:
        print('O aluno foi reprovado!')

if __name__ == '__main__':
    main()