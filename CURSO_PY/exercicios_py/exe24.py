
vendas = [100, 250, 80, 300, 150]

i = 0
total = 0
quantidade = 0

while i < len(vendas):
    print(vendas[i])
    total = total + vendas[i]

    
    if vendas[i] > 150:
        quantidade += 1

    i += 1
        
print('Total acima de 150: ',total)
print('Quantidade superiores: ',quantidade)
