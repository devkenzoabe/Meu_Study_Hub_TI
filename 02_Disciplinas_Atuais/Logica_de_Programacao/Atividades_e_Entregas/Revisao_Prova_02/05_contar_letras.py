# Peça uma palavra e conte quantas letras ela tem usando for, sem usar len().
palavra = str(input('Digite uma palavra: '))
qtd = 0

for letra in palavra:
    qtd += 1

print(f'\nA palavra {palavra} tem {qtd} letras!')
