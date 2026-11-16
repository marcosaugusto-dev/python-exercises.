preco_valido = False

while preco_valido == False:
    try:
        preco_produto = float(input('Digite o valor do produto: '))

        if preco_produto <= 0:
            print('Preco invalido!')

        else:
            print('Preço cadastrado com sucesso! ')
            preco_valido = True

    except ValueError:
        print('Digite um valor numérico válido!')