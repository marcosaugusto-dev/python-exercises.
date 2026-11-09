# Faça um programa que:
# Peça uma temperatura em Celsius.
# Converta para Fahrenheit.

celsius = float(input('Digite a temperatura em celsius: '))
fahren = celsius * 1.8 + 32

print('A conversao deu {}'.format(fahren))