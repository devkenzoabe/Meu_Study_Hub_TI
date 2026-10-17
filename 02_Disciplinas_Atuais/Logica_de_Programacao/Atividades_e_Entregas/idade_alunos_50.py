ct_alunos = 0
soma_idade = 0
alunos_menores_idade = 0
mais_novo = float('inf')
mais_velho = float('-inf')

for i in range(0,5):
    idade = int(input(f'\nDigite a idade do aluno {i + 1}: '))
    ct_alunos += 1
    soma_idade += idade

    if idade < 18:
        alunos_menores_idade += 1

    if idade < mais_novo:
        mais_novo = idade

    if idade > mais_velho:
        mais_velho = idade

media_idade = soma_idade / ct_alunos

print('\n============= Estatísticas =============')
print(f'Soma das idades dos alunos: {soma_idade}')
print(f'Média Aritmética dos alunos: {media_idade}')
print(f'Idade do aluno mais novo: {mais_novo}')
print(f'Idade do aluno mais velho: {mais_velho}')
print(f'Quantidade de alunos menores de idade: {alunos_menores_idade}')