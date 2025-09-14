n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

restoDivisão = n1 % n2

if restoDivisão == 0:
    print(n1, "é divisível por",n2)
else:
    print(n1, "não é divisível por",n2)
