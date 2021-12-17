
import adivinhacao
import forca

def escolha_jogos():
    print("bem-vindo ao repositório de jogos")
    jogo = int(input("(1) para jogo da adivinhação \n(2) para jogo da forca \ndigite um número para escolher o jogo:  "))

    if jogo == 1:
        print("jogo da adivinhação")
        adivinhacao.jogo()
    elif jogo == 2: 
        print("jogo da forca")
        forca.jogo()

if (__name__ == "__main__"):
    escolha_jogos()