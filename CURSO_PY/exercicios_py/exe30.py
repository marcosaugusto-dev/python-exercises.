
idade_valida = False

while idade_valida == False:
    try:
        idade = int(input('Digite sua idade: '))

        if idade <= 0:
            print('Idade invalida!')

        else:
            idade_valida = True
            print('Idade cadastrada!')

    except ValueError:
        print('Digite apenas sua idade!')