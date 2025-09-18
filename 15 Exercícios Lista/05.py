lista = []
control = int

while control != 0:
    print("Lista de Compras em Python: \n Digite 1 para adicionar um produto. \n Digite 2 para ver um produto. \n Digite 3 para atualizar um produto. \n Digite 4 para deletar um produto. \n Digite 0 para sair." )

    ncont = int(input("Digite uma opção: "))

    if ncont == 1:
        product = input("Digite o nome do produto: ")

        lista.append(product)

        print("Lista atualizada: ", lista)
    elif ncont == 2:
        productName = int(input("Digite o nome do produto que deseja visualizar:"))

        print("O produto está no índice: ", lista.index(productName))
    elif ncont == 3:
        productIndex = int(input("Digite o nome do produto que deseja visualizar:"))

        newProduct = str(input("Digite o nome do produto que irá sibstituir o indice digitado: "))

        lista.insert(productIndex, newProduct)

        print("Lista atualizada: ", lista)
    elif ncont == 4:
        productIndex = int(input("Digite o indice do produto que deseja apagar:"))
        
        lista.remove(productIndex)

        print("Lista atualizada: ", lista)
    elif ncont == 0:
        break
    