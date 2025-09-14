dia = int(input("Digite um dia: "))
mes = str(input("Digite um mês: "))
ano = int(input("Digite um ano: "))

if dia == 31:
    if mes == "Abril" or mes == "Junho" or mes == "Setembro" or mes == "Novembro":
        print("Data inválida.")
    else:
        print(dia, "de", mes, "de", ano)
elif dia >= 1 and dia <= 30:
    if mes == "Janeiro" or mes == "Março" or mes == "Maio" or mes == "Junho" or mes == "Agosto" or mes == "Outubro" or mes == "Dezembro":
        print("Data inválida.")
    else:
        print(dia, "de", mes, "de", ano)