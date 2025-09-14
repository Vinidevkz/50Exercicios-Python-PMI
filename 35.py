a1 = int(input("Digite o primeiro lado do triângulo:"))
a2 = int(input("Digite o segundo lado do triângulo:"))
a3 = int(input("Digite o terceiro lado do triângulo:"))

if a1 == a2 and a2 == a3:
    print("O triângulo é equilátero.")
elif a1 == a2 and a2 != a3 or a1 != a2 and a2 == a3:
    print("O triângulo é Isósceles.")
else:
    print("O triângulo é escaleno.")
