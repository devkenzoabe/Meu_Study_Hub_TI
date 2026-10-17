nome_produto = input('Digite o nome do produto:')
valor_compra = float(input('Digite o valor do produto: '))
valor_venda = float(input('Digite o valor de venda: '))

if valor_venda > valor_compra:
    lucro = valor_venda - valor_compra
    print(f'{nome_produto} teve lucro de R${lucro} = {valor_venda} - {valor_compra}')
elif valor_compra > valor_venda:
    prejuizo = valor_compra - valor_venda
    print(f'{nome_produto} teve prejuízo de R${prejuizo} = {valor_venda} - {valor_compra}!')
else:
    print('Os valores são iguais!')
    