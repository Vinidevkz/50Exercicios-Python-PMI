print("Bem-Vindo(a) ao Jogo da Velha!")

tabuleiro = ["-"] * 9

itsOver = 0
smbJogada = "X"

while itsOver != 1:

    print("Digite a casa que deseja colocar o ",smbJogada, ":")
    print("0, 1 e 2:", tabuleiro[0] , "/" , tabuleiro[1] , "/", tabuleiro[2])
    print("3, 4 e 5:", tabuleiro[3] , "/" , tabuleiro[4] , "/", tabuleiro[5])
    print("6, 7 e 8:", tabuleiro[6] , "/" , tabuleiro[7] , "/", tabuleiro[8])
    jogada = int(input())

    tabuleiro[jogada] = smbJogada

    smbJogada = "O" if smbJogada == "X" else "X"

    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] and tabuleiro[0] is not "-" or tabuleiro[3] == tabuleiro[4] == tabuleiro[5] and tabuleiro[3] is not "-" or tabuleiro[6] == tabuleiro[7] == tabuleiro[8] and tabuleiro[6] is not "-" or tabuleiro[0] == tabuleiro[4] == tabuleiro[8] and tabuleiro[0] is not "-" or tabuleiro[2] == tabuleiro[4] == tabuleiro[6] and tabuleiro[2] is not "-" or tabuleiro[0] == tabuleiro[3] == tabuleiro[6]and tabuleiro[0] is not "-" or tabuleiro[1] == tabuleiro[4] == tabuleiro[7]and tabuleiro[1] is not "-" or tabuleiro[2] == tabuleiro[5] == tabuleiro[8] and tabuleiro[2] is not "-":
        print("")
        print("### FIM DE JOGO ###")
        print(tabuleiro[0] , "/" , tabuleiro[1] , "/", tabuleiro[2])
        print(tabuleiro[3] , "/" , tabuleiro[4] , "/", tabuleiro[5])
        print(tabuleiro[6] , "/" , tabuleiro[7] , "/", tabuleiro[8])
        print("###")
        print(tabuleiro[0], "venceu!")
        print("### FIM DE JOGO ###")
        print("")
        itsOver = 1
    elif all(casa is not "-" for casa in tabuleiro):
        print("Empate!")
        isOver = 1