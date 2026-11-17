nota_valida = False

while nota_valida == False:
    try:
        nota = float(input('Digite sua nota: '))

        if nota < 0 or nota > 10:
            print('Nota invalida!')

        else:
            nota_valida = True
            print('Nota cadastrada')
            print(f'Nota: {nota}')

    except ValueError:
        print('Digite apenas sua nota com apenas numeros decimais')
