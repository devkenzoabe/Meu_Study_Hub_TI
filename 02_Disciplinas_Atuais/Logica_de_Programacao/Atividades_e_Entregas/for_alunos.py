total_alunos = 5
soma_notas = 0
alunos_aprovados = 0
alunos_reprovados = 0

for i in range(total_alunos): #range(1, 6, 1) - range(0, total_alunos)
    nota = float(input('\nDigite a nota do aluno: '))
    if nota >= 5:
        alunos_aprovados += 1
    else:
        alunos_reprovados += 1

    soma_notas += nota

media_notas = soma_notas/total_alunos

print(f'\nSoma das notas: {soma_notas:.2f}')
print(f'Quantidade de notas: {total_alunos}')
print(f'Media das notas: {media_notas:.2f}')
print(f'Alunos aprovados: {alunos_aprovados}')
print(f'Alunos reprovados: {alunos_reprovados}')


