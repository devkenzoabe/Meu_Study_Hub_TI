"""Desenvolva o programa que calcule a média aritmética de uma turma,
onde cada aluno realizou uma avaliação. Não sabemos a quantidade de
alunos, por isso usaremos o valor “-1” como condição (flag) de saída.
Na tela de saída, mostre a média aritmética da turma e a quantidade
de alunos da turma.
Analise o problema e verifique quais são os dados que o usuário precisa
fornecer (digitar) como entrada."""

lista_notas = []

print('\nDigite [-1] para sair!')

while True:
    nota = float(input('\nDigite a nota do aluno: '))
    if nota == -1.0:
        break

    lista_notas.append(nota)

soma_notas = sum(lista_notas)
qtd_alunos = len(lista_notas)
media_notas = soma_notas/qtd_alunos

print(f'\nMédia da turma: {media_notas:.2f}')
print(f'\nQuantidade de alunos: {qtd_alunos}')