char = input("Digite uma letra:")
tamanho = len(char)
 
if tamanho > 1:
    print("Digite apenas um caractere.")
else:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" :
        print("O caractere é um vogal.")
    else:
        print("O caractere é uma consoante.")