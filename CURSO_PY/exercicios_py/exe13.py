
# Exercicio 04 - Tabuada

numero = int(input('Digite um numero de 1 a 10: '))

if numero < 1 or numero > 10:
    print('Numero invalido')

else:
    for i in range(1, 11):
        resultado = numero * i
        print('{} x {} = {}'.format(numero, i, resultado))
