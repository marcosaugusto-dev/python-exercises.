vendas = [150, 80, 250, 100, 300, 50, 200]

total = 0
media = 0
maior = vendas[0]
menor = vendas[0]
maiores = 0
contador = 0

for venda in vendas:
    total += venda
    contador += 1

    if venda > maior:
        maior = venda

    if venda < menor:
        menor = venda

    if venda > 150:
        maiores += 1

media = total / contador
print(f'Total: {total}')
print('Quantidade: ',len(vendas))
print(f'Media: {media}')
print(f'Maior venda: {maior}')
print(f'Menor venda: {menor}')
print(f'Quantidade maior de 150: {maiores}')