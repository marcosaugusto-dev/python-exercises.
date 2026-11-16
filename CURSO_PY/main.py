# Crie um programa que:
# 1. Solicite um preço de produto.
# 2. Utilize float() para aceitar valores decimais.
# 3. Utilize try/except para tratar entradas inválidas.
# 4. Se o preço for menor ou igual a zero, mostre "Preço inválido!".
# 5. Se for válido, mostre "Preço cadastrado com sucesso!".
# 6. Continue solicitando até receber um preço válido.
# # Dica: utilize preco_valido = False e while.

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