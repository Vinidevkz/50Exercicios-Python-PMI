n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("Digite: \n 1: Soma \n 2: Subtração \n 3: Multiplicação \n 4: Divisão")
tipoCalculo = int(input("Digite:"))

if tipoCalculo == 1:
    resultado = n1 + n2
    print(resultado)
elif tipoCalculo == 2:
    resultado = n1 - n2
    print(resultado)
elif tipoCalculo == 3:
    resultado = n1 * n2
    print(resultado)
elif tipoCalculo == 4:
    resultado = n1 / n2
    print(resultado)
else:
    print("Número inválido.") 