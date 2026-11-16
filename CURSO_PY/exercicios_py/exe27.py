contador = 0

while contador < 3:
    print('Tentativa:', contador + 1)
    contador += 1

    try:
        idade = int(input('Digite sua idade: '))
        if idade <= 0:
            print('Idade invalida')
        elif idade >= 18:
             print('Maior de idade.')
             break
        else:
            print('Menor de idade.')
            break
    
    except ValueError:
        print('Digite apenas sua idade.')