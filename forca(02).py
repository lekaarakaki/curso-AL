import random


def jogar():
    print("bem-vindo ao jogo da forca!")

    
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    enforcou = False 
    acertou = False
    erro = 0 


    while(not enforcou and not acertou):
        chute = pede_chute()
        
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        else:
            erro +=1
            desenha_forca(erro)

        enforcou = erro == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        mensagem_vitoria()
    else:
        mensagem_perdeu(palavra_secreta)
    print("fim do jogo")



def carregar_palavra_secreta():
    arquivo = open("palavra.txt", "r")
    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta

def inicializar_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_chute(): 
    chute = input("chute uma letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
                
        if (chute == letra):
            letras_acertadas[index] = letra
        index +=1
        
def mensagem_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensagem_vitoria():

    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):

    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()
