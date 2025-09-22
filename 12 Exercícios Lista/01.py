try:
    numero = int(input("Digite seu número de telefone sem parênteses e traços (tudo junto):"))

    if numero < 11 or numero > 11:
        print("Número inválido.")
    else:
        digitos = str(numero)[:2]
        digitos1 = str(numero)[2:7]
        digitos2 = str(numero)[7:11]
        print("({}) {} - {}".format(digitos, digitos1, digitos2))
except:
    print("Dígitos Inválidos.")
