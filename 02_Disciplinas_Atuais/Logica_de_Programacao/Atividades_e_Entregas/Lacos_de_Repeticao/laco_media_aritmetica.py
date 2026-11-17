alunos = 0
soma_notas = 0

nome_disciplina = input('\nDigite o nome da disciplina: ')

print('\nDigite [-1] para sair da repetição')

while True:
    notas = float(input('\nDigite as notas dos alunos: '))
    if notas == -1:
        break
    alunos = alunos + 1
    soma_notas = soma_notas + notas

print('\nQuantidade de alunos:', alunos)
print('\nSoma das notas dos alunos:', soma_notas)

media = soma_notas / alunos

print('\nMédia da sala:', f'{media:.2f}')

print('\nCálculo da Discilplina:', nome_disciplina)

