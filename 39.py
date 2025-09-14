userName = "viniedu"
password = "123fatec"

loginUserName = str(input("Digite seu nome de usuário:"))
loginPassword = str(input("Digite sua senha:"))

if loginUserName == userName and loginPassword == password:
    print("Usuário logado com sucesso.")
else:
    print("Credenciais incorretas.")