print("Biblioteca. Digite: \n 1: Ver Livros disponíveis. \n 2: Pegar um livro. \n 3: Ver meus livros. \n 4: Devolver um Livro.")

livros = ["Harry Potter", "O Senhor dos Anéis", "Duna"]
meusLivros = []

def verLivros():
    return "Livros no sistema:", livros

def pegarUmLivro(index):
    meusLivros.append(livros[index])
    livros.pop(index)
    return "Minha lista atualizada: ", meusLivros

def devolverLivro(index):
    livros.append(meusLivros[index])
    meusLivros.pop(index)
    return "Livro devolvido com sucesso. Minha lista atualizada: ", meusLivros

n = 1

while n != 0:

    n = int(input("Digite o número: "))

    if n == 1:
        print(verLivros())
    elif n == 2:
        i = int(input("Digite o index do livro que deseja pegar: "))
        print(pegarUmLivro(i))
    elif n == 3:
        print("Seus livros: ", meusLivros)
    elif n == 4:
        i = int(input("Digite o index do livro que deseja devolver: "))
        print(devolverLivro(i))
    elif n == 0:
        break


