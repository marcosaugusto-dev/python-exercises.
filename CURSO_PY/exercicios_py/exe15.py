
# Desafio integrador - Analise de numeros

soma = 0
par = 0
impar = 0
maior = None
menor = None

for i in range(1, 6):
    numero = int(input('Digite um numero: '))
    soma = soma + numero

    if numero % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

    if maior is None:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

print('RESULTADOS\n')
print('Soma:', soma)
print('Pares:', par)
print('Impares:', impar)
print('Maior:', maior)
print('Menor:', menor)
