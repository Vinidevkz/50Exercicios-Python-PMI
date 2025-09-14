n1 = int(input("Digite um número: "))

restoDivisao3 = n1 % 3
restoDivisao5 = n1 % 5

if restoDivisao3 == 0 and restoDivisao5 == 0:
    print("O número é divisivel por 3 e por 5.")
else:
    print("O número não é divisível pro 3 e por 5.")
