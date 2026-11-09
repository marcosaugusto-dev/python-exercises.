N1 = float(input('Digite um numero: '))
N2 = float(input('Digite outro numero: '))
operador =str(input('Digite o operador + - * /: '))

if (operador == '+'):
    soma = N1 + N2
    print('A soma de {} e {} deu:{}'.format(N1,N2,soma))

elif (operador == '-'):
    subt = N1 - N2
    print('A subtracao de {} e {} deu:{}'.format(N1,N2,subt))

elif (operador == '*'):
    mult = N1 * N2
    print('A multiplicacao de {} e {} deu:{}'.format(N1,N2,mult))

elif (operador == '/'):
    if (N2 != 0):
        divi = N1 / N2 
        print('A divisao de {} e {} deu:{}'.format(N1,N2,divi))
    else:
        print('NAO E POSSIVEL DIVIDIR POR ZERO')

else:
    print('Operador invalido') 
