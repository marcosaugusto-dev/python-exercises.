estoque = 0

while True:
    produto = int(input('Digite a quantidade de produtos que chegaram: '))

    if produto < 0:
        print('Número negativo, digite novamente.')
        continue

    if produto == 0:
        print('Programa encerrado.')
        print(f'Estoque final: {estoque}')
        break

    for i in range(1, produto + 1):
        print(f'Produto {i} recebido')

    estoque = estoque + produto
    print(f'Estoque atual: {estoque}\n')