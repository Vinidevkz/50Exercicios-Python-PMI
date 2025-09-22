print("Cadastro de Clientes: \n")

nomeValidated = 0
emailValidated = 0
passwordValidated = 0
descValidated = 0

while nomeValidated != 1:
    nomeCliente = str(input("Digite o nome do cliente (min: 15 caracteres):"))

    if len(nomeCliente) < 15:
        print("Nome inválido.")
    else:
        while emailValidated != 1:
            emailCliente = str(input("Digite o email do cliente:"))

            if not "@gmail.com" in emailCliente:
                print("Email inválido.")
            else:
                while passwordValidated != 1:
                    passowordCliente = str(input("Digite a senha do cliente (min: 15 caracteres):"))

                    if len(passowordCliente) < 15:
                        print("Senha inválida.")
                    else:
                        print("Cliente criado com sucesso: \n Nome:", nomeCliente, "\n Email:", emailCliente, "\n Senha:", passowordCliente)
                        nomeValidated = 1
                        emailValidated = 1
                        passwordValidated = 1
