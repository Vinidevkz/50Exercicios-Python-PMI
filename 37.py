precoProduto = int(print("Digite o preço do produto:"))

if precoProduto <= 500 and precoProduto < 1000:
    total = precoProduto - ((precoProduto * 10) / 100)
    print(total)
elif precoProduto >= 1000 and precoProduto < 1500:
    total = precoProduto - ((precoProduto * 15) / 100)
    print(total)
elif precoProduto >= 1500 and precoProduto < 2000:
    total = precoProduto - ((precoProduto * 20) / 100)
    print(total)
else:
    total = precoProduto - ((precoProduto * 25) / 100)
    print(total)   