# Crie uma função dobro(numero) que receba um número e retorne o dobro. Na função principal, chame a função e mostre o resultado.
def dobro(numero):
    return numero * 2

    

def main():
    numero = float(input('Digite um número: '))
    resultado_dobro = dobro(numero)
    print(f'O dobro do número {numero} é {resultado_dobro}')

if __name__ == '__main__':
    main()