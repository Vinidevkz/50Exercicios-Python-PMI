ano = int(input("Digite um ano:"))

isBissexto = ano % 4

if isBissexto == 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")