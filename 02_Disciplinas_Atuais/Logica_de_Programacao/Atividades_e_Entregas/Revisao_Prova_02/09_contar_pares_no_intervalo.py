# Crie uma função que receba dois números, início e fim, e conte quantos números pares existem entre eles, incluindo os extremos.
def contar_pares(a, b):
    ct_pares = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            ct_pares += 1
    return ct_pares 

def main():
    valor1 = int(input('\nDigite o primeiro número: '))      
    valor2 = int(input('Digite o segundo número: '))     

    print(f'\nQuantidade de número pares no intervalo: {contar_pares(valor1, valor2)}')
        
if __name__ == '__main__':
    main()
