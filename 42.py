x = int(input("Digite X: "))
y = int(input("Digite Y: "))

if x > 0 and y > 0:
    print("Primeiro quadrante.")
elif x < 0 and y > 0:
    print("Segundo quadrante.")
elif x < 0 and y < 0:
    print("Terceiro quadrante.")
elif x > 0 and y < 0:
    print("Quarto quadrante.")