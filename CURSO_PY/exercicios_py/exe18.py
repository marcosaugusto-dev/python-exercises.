produtos = ["Arroz", "Feijão", "Macarrão", "Leite", "Café"]
print('Lista completa:',produtos)
print('Primeiro da lista:',produtos[0])
print('Terceiro da lista:',produtos[2])
print('Ultimo da lista:',produtos[4])

produto = input('Digite um novo produto: ')

produtos.append(produto)

print('Lista atualizada:',produtos)

rem_produto = input('Digite o produto que deseja remover: ')

produtos.remove(rem_produto)

print('Lista atualizada:',produtos)

remove2 = int(input('Digite a posição do produto que deseja excluir:'))

produtos.pop(remove2)

print('Lista atualizada:',produtos)


quantidade = len(produtos)

print('Quantidade de produtos atualizado:',quantidade)

consulta = input('Qual produto voce deseja consultar: ')

quantidade_produto = produtos.count(consulta)

print('Quantidade: ', quantidade_produto)


posicao = input('Digite o produto que deseja encontrar: ')

produto_pos = produtos.index(posicao)

print('Posicao do produto:',produto_pos)

inserir = input('Digite qual produto voce deseja inserir:')
inserir_pos = int(input('Digite a posicao de onde deseja inserir:'))


produtos.insert(inserir_pos,inserir)

print('Lista atualizada:',produtos)


produtos.sort()

print('Lista em ordem:',produtos)


produtos.reverse()


print('Lista em ordem reversa: ',produtos)

novos_produtos = ["Açúcar", "Óleo", "Farinha"]

produtos.extend(novos_produtos)


print('Lista com os novos produtos:',produtos)


copia_produtos = produtos.copy()

copia_produtos.append('agua')

print('Lista original:',produtos)
print('Lista copiada:',copia_produtos)

copia_produtos.clear()
print('Lista copiada sem nada:',copia_produtos)


