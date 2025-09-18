try:
    n1 = int(input("Digite um número:"))

    binario = bin(n1)
    octal = oct(n1)
    hex = hex(n1)

    print("Deciamal:",n1, "Binário:",binario, "Octal:",octal, "Hexadecimal:",hex)
except:
    print("Número inválido.")