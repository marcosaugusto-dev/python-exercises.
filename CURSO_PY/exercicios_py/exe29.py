
nome = input('Digite seu nome: ').strip()

if nome == '':
    print('Nome invalido.')

else:
    try:
        idade = int(input('Digite sua idade: '))

        if idade <= 0:
            print('Idade invalida.')

        else:
            print('Funcionario cadastrado com sucesso.')
            print(f'Funcionario {nome}')
            print(f'Idade: {idade}')
    
    except ValueError:
        print('Digite uma idade válida, usando apenas números inteiros.')