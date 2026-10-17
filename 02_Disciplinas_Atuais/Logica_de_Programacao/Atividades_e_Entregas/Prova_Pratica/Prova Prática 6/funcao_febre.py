def verificar_febre(temperatura):
    if temperatura >= 37.8:
        return True
    else:
        return False


def main():
    temperatura_paciente = float(input('\nDigite a temperatura do paciente: '))
    resultado_febre = verificar_febre(temperatura_paciente)

    if resultado_febre:
        print('O paciente está com febre!')
    else:
        print('O paciente não está com febre!')


if __name__ == '__main__':
    main()