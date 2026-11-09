# 5. Maior de dois números
# Leia dois números e mostre qual é o maior. Se forem iguais, avise.

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))

if n1 > n2:
    print(f'O numero {n1} e maior.')

elif n2 > n1:
    print(f'O numero {n2} e maior.')

else:
    print('Os numero sao iguais.')abri