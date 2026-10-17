ct_candidato1 = 0
ct_candidato2 = 0
ct_candidato3 = 0
ct_nulo = 0
ct_branco = 0

print('\nDigite [0] para sair')

while True:
    voto = int(input('\nDigite seu voto:\n[1] Candidato 1\n[2] Candidato 2\n[3] Candidato 3\n[5] Voto Nulo\n[6] Voto em Branco\nOpção: '))
    if voto == 0:
        break

    if voto == 1:
        ct_candidato1 += 1
    elif voto == 2:
        ct_candidato2 += 1
    elif voto == 3:
        ct_candidato3 += 1
    elif voto == 5:
        ct_nulo += 1
    elif voto == 6:
        ct_branco += 1
    else:
        print('Você digitou um valor inválido!')

def palavra_votos(quantidade):
    if quantidade == 1:
        return 'voto'
    else:
        return 'votos'

print(f'\nVotos Candidato 1: {ct_candidato1} {palavra_votos(ct_candidato1)}')
print(f'Votos Candidato 2: {ct_candidato2} {palavra_votos(ct_candidato2)}')
print(f'Votos Candidato 3: {ct_candidato3} {palavra_votos(ct_candidato3)}')
print(f'Votos Nulos: {ct_nulo}')
print(f'Votos em Branco: {ct_branco}')