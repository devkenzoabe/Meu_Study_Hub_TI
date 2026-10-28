numero_alunos = 0
alunos_aprovados = 0
alunos_reprovados = 0
valor_notas = 0

print('Digite [-1] para sair')

while True:
    notas = float(input('\nDigite o valor das notas: '))
    if notas == -1:
        break
    if notas >= 5:
        alunos_aprovados += 1
        numero_alunos += 1
        valor_notas += notas
    elif notas < 5:
        alunos_reprovados += 1
        numero_alunos += 1
        valor_notas += notas

media_notas = valor_notas / numero_alunos

print('\nQuantidade de alunos que fizeram a prova:', numero_alunos)
print('Quantidade de alunos aprovados:', alunos_aprovados)
print('Quantidade de alunos reprovados:', alunos_reprovados)
print('Média da turma:', f'{media_notas:.2f}')
