cpf = str(input("Digite seu CPF:"))

if len(cpf) < 14 and len(cpf) > 14:
    print("CPF inválido.")
elif cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
    if cpf[10] == 1:
        print("Seu CPF pertence a DF, GO, MS, MT, TO:", cpf)
    elif cpf[10] == 2:
        print("Seu CPF pertence a AC, AM, AP, PA, RO e RR:", cpf)
    elif cpf[10] == 3:
        print("Seu CPF pertence a CE, MA e PI:", cpf)
    elif cpf[10] == 4:
        print("Seu CPF pertence a Al, PB, PE, RN:", cpf)
    elif cpf[10] == 5:
        print("Seu CPF pertence a BA e SE:", cpf)
    elif cpf[10] == 6:
        print("Seu CPF pertence a MG:", cpf)
    elif cpf[10] == 7:
        print("Seu CPF pertence a ES e RJ:", cpf)
    elif cpf[10] == 8:
        print("Seu CPF pertence a SP:", cpf)
    elif cpf[10] == 9:
        print("Seu CPF pertence a PR e SC:", cpf)
    elif cpf[10] == 0:
        print("Seu CPF pertence a RS:", cpf)