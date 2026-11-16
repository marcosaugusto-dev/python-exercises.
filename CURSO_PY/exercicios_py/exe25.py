gastos = [35, 120, 50, 200, 80, 150, 40]

i = 0
total = 0
quantidade = 0

while i < len(gastos):
    total = total + gastos[i]
    print(gastos[i])
    if gastos[i] > 100:
        quantidade += 1
        
    i += 1

    media = total / len(gastos)


print('Quantidade maiores que 100: ',quantidade)
print('Media: ',media)