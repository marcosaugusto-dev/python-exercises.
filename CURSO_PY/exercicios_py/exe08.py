# Peça dois números ao usuário e mostre qual é o maior.
# Se forem iguais, mostre "Os números são iguais".

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))

if (n1 > n2):
    print('O numero {} e maior'.format(n1))

elif (n2 > n1):
    print('O numero {} e maior'.format(n2))

else:
    print('Os numeros sao iguais')

