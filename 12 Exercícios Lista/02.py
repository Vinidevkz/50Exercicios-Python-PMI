try:
    nota1 = int(input("Digite a primeira nota:"))
    try:
        nota2 = int(input("Digite a segunda nota:"))
        try:
            nota3 = int(input("Digite um terceiro nota:"))

            media = (nota1 + nota2 + nota3) / 3

            if media < 3:
                print("REPROVADO.")
            elif media >= 3 and media < 6:
                print("RETIDO.")
            else:
                print("APROVADO.")
        except:
            print("Digite um número válido.")
    except:
        print("Digite um número válido.")
except:
    print("Digite um número válido.")