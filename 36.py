password = int(input("Digite sua senha:"))

verifyPassword = int(input("Verifique sua senha:"))

if verifyPassword == password:
    print("Senha correta e verificada.")
else:
    print("Senha incorreta.")