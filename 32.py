peso = 75
altura = 1.85

imc = peso // (altura ** 2)

if imc < 18.5:
    print("Baixo peso.")
elif imc == 18.5 or imc <= 24.9:
    print("Peso normal ou Eutrófico.")
elif imc == 25.0 or imc <= 29.9:
    print("Sobrepeso.")
elif imc == 30.0 or imc <= 34.9:
    print("Obesidade Grau 1.")
elif imc == 35.0 or imc <= 39.9:
    print("Obesidade Grau 2.")
else:
    print("Obesidade Grau 3.")