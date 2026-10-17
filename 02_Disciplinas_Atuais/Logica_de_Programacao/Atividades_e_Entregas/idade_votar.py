nome_usuario = input('Digite o seu nome:')
ano_usuario = int(input('Digite seu ano de nascimento:'))
print('Ano de nascimento do usuário:', ano_usuario)
idade_usuario = 2026 - ano_usuario
print('Idade do usuário:', idade_usuario)

if idade_usuario >= 18:
    print(f'{nome_usuario}, você pode votar!')
    print(f'{nome_usuario}, você pode tirar a CNH!')
elif idade_usuario >= 16:
    print(f'{nome_usuario}, você pode votar!')
    print(f'{nome_usuario}, você não pode tirar a CNH!')
else:
    print(f'{nome_usuario}, você não pode votar!')
    print(f'{nome_usuario}, você não pode tirar a CNH!')
