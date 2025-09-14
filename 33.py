intervalo1 = int(input("Digite o primeiro intervalo: "))
intervalo2 = int(input("Digite o segundo intervalo: "))

n = int(input("Digite um número qualquer: "))

if n >= intervalo1 and n <= intervalo2:
    print("O número está no intervalo entre",intervalo1,"e",intervalo2)
else:
    print("O número não está no intervalo.")