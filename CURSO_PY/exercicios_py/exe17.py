produtos = ["Arroz","Feijao","Macarrao","Leite","Cafe"]

print(produtos)
print('Primeiro produto: ',produtos[0])
print('Terceiro produto: ',produtos[2])
print('Ultimo produto: ',produtos[4])

produto = int(input('Digite um novo produto: '))

produto_rem = produtos.pop(produto)
        

print('Lista atualiza: ',produtos)