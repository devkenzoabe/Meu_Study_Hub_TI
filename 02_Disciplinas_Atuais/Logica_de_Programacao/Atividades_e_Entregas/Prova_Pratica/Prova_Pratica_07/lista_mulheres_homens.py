"""Elabore o programa que leia a altura e o gênero (‘m’ para masculino e ‘f’ para feminino) de um grupo de pessoas. Gere a tela de saída com as seguintes informações: maior altura do grupo (de todas as pessoas), menor altura do grupo (de todas as pessoas), quantidade de homens e quantidade de mulheres.
 Analise o problema e verifique quais são os dados que o usuário precisa fornecer (digitar) como entrada."""

lista_homens = []
lista_mulheres = []
lista_alturas = []

print('\nDigite [0] para sair!')

while True:
    altura = float(input('\nDigite a altura da pessoa: '))
    if altura == 0.0:
        break

    lista_alturas.append(altura)

    genero = str(input('\nDigite o gênero da pessoa:\n[m] - masculino\n[f] - feminino\n'))
    if genero == 'm':
        lista_homens.append(genero)
    elif genero == 'f':
        lista_mulheres.append(genero)
    else:
        print('\nResposta Inválida!')

if len(lista_alturas) > 0:
    maior_altura = max(lista_alturas)
    menor_altura = min(lista_alturas)
    qtd_homens = len(lista_homens)
    qtd_mulheres = len(lista_mulheres)

    print(f'\nMaior altura do grupo: {maior_altura}')
    print(f'Menor altura do grupo: {menor_altura}')
    print(f'Quantidade de homens: {qtd_homens}')
    print(f'Quantidade de mulheres: {qtd_mulheres}')
else:
    print('\nNenhum dado foi registrado!')