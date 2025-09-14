palavraSecreta = "Python"

print("Dica: A palavra secreta tem ", len(palavraSecreta), "letras e\né sobre tecnologia.")

palpite = ""

while palpite != palavraSecreta:
    palpite = str(input("Digite um palpite: "))

    if palpite != palavraSecreta:
        print("Você errou! :(. Tente novamente!")

print("Você acertou!")
