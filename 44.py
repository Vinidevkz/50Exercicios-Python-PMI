idade = int(input("Digite sua idade: "))

if idade < 8:
    print("Menores de 8 anos não pagam.")
elif idade >= 8 and idade < 14:
    print("A passagem custará 10 reais.")
elif idade >= 14 and idade < 18:
    print("A passagem custará 15 reais.")
else:
    print("A passagem custará 20 reais.")