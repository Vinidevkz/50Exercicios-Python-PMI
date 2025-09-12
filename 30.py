nota = float(input("Digite a nota do aluno: "))

if(nota < 3):
    print("REPROVADO.")
elif(nota >= 3 and nota < 6):
    print("RETIDO.")
else:
    print("APROVADO.")
