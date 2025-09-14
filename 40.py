temp = int(print("Digite uma temperatura em C° :"))

if temp < 15:
    print("Está frio.")
elif temp >= 15 or temp < 25:
    print("Clima agradável.")
elif temp >= 25 or temp < 30:
    print("Está calor.")
else:
    print("Está muito calor.")