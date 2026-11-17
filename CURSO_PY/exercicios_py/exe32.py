notas = []
nomes = []
contador = 0

while contador < 3:
    try:
        nome = input('Digite seu nome: ')
        nota = float(input('Digite sua nota:')) 

        if nota < 0 or nota > 10:
            print('Nota inválida! Digite uma nota entre 0 e 10.')

        else:
            contador += 1
            nomes.append(nome)
            notas.append(nota)

    except ValueError:
         print('Digite apenas dados corretos.')


print('Dados cadastrados!')
for i in range(len(nomes)):
    print('Nome:', nomes[i])
    print('Nota:', notas[i])