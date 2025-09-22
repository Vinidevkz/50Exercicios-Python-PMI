texto = "Olá Senhor Alfredo! Bom dia!."

totalCaracteres = len(texto)

def totalPalavras(text):
    i = 0
    wordCount = 1

    while i < len(text):
        if text[i] == " ":
            wordCount = wordCount + 1
        i = i + 1

    return wordCount

def totalFrases(text):
    i = 0
    sentenceCount = 1

    while i < len(text):
        if text[i] == ".":
            sentenceCount = sentenceCount + 1
        i = i + 1

    return sentenceCount


print("Caracteres: ", totalCaracteres, "\nPalavras: ", totalPalavras(texto), "\nFrases: ", totalFrases(texto)) 