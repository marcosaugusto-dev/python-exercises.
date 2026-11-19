# 1. Nome do produto.
# 2. Preço do produto.
# 3. Quantidade em estoque.
# Regras de validação:
# - Nome não pode ficar vazio.
# - Preço precisa ser numérico.
# - Preço não pode ser igual ou inferior a zero.
# - Quantidade precisa ser um número inteiro.

produto_valido = False

while produto_valido == False:
    try:
        nome = input('Digite o nome do produto: ').strip()

        if nome == '':
            print('Nome invalido!')
        
        else:
            preco = float(input('Digite o preço do produto: '))
            
            if preco <= 0:
                print('Preco invalido')
        
            else:
                while produto_valido == False:
                    try:
                        quantidade = int(input('Digite a quantidade do produto: '))
                        if quantidade <= 0:
                            print('Quantidade invalida!')

                        else:
                            produto_valido = True
                            print('Produto cadastrado com sucesso')
                    
                    except ValueError:
                        print('Digite o valor correto')

    except ValueError:
        print('Digite os dados corretos')


