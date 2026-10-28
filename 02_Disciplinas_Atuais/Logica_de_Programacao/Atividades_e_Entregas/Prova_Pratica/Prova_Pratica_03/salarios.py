ct_funcionarios_menor5 = 0
ct_funcionarios_5_menor10 = 0
ct_funcionarios_maior10 = 0
folha_salarial = 0

print('\nDigite [0] para sair')
salario_minimo = float(input('\nDigite o valor do salário mínimo: '))

while True:
    salario = float(input('\nDigite o salário do funcionario: '))
    if salario == 0:
        break
    if salario < salario_minimo * 5:
        ct_funcionarios_menor5 += 1
    elif salario_minimo * 5 <= salario < salario_minimo * 10: # = salario >= salario_minimo * 5 and salario < salario_minimo * 10
        ct_funcionarios_5_menor10 += 1
    else:
        ct_funcionarios_maior10 += 1

    folha_salarial += salario

print(f'\nFuncionários que ganham menos que 5 salários mínimos: {ct_funcionarios_menor5}')
print(f'Funcionários que ganham de 5 até 10 salários mínimos: {ct_funcionarios_5_menor10}')
print(f'Funcionários que ganham 10 ou mais salários mínimos: {ct_funcionarios_maior10}')
print(f'Folha salarial da empresa: {folha_salarial}')
