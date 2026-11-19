notas = [7, 8, 5, 9, 6, 10]

total = 0
media = 0  
maior = notas[0]
menor = notas[0]
alunos = 0
contador = 0
aprovado = 0
reprovado = 0

for nota in notas:
    total += nota
    contador += 1

    if nota > maior:
        maior = nota

    if nota < menor:
        menor = nota 

    if nota >= 7:
        aprovado += 1

    else:
        reprovado += 1

media = total / contador
print('Alunos:',len(notas)) 
print(f'Total: {total}')
print(f'Media: {media}')
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
print(f'Aprovados: {aprovado}')
print(f'Reprovados: {reprovado}')
