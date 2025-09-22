passwordVerified = 0

while passwordVerified != 1:
    password = str(input("Digite sua senha: "))

    if len(password) < 10:
        print("A senha é muito curta.")
    elif "#" in password or "!" in password or "&" in password:
        print("Sua senha foi gerada com sucesso!:", password)
        passwordVerified = 1
    else:
        print("A senha precisa ter algum caractere especial e números.")