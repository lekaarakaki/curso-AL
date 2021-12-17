# descrição do programa: jogo de advinhação de número.
import random 
def jogo( ):

    print("Bem-vindo ao jogo da adivinhação.") #começo do jogo

    print("\nadivinhe o número que estou pensando.") #descrição do jogo
    x = random.randint(0, 100) #escolha do número a ser encontrado
   
    print("niveis de dificuldades:\n(1) fácil (2)médio (3) difício") #escolha do nivel de dificuldade do jogo
    nivel = input("defina o nível: ")

    if nivel == "1":
        tentativas = 10
        pontos = 10
    elif nivel =="2":
        tentativas = 5
        pontos = 5
    elif nivel == "3":
        tentativas = 3
        pontos = 3
    print(x)

    for rodada in range (1, tentativas+1): #rodadadas do jogo
        print("tentativa {} de {}".format(rodada , tentativas) )
        chute = int(input("digite um número inteiro de 0 à 100: " ))
        if chute != x:
            pontos = pontos - 1

        if chute <0 or chute >100: #dicas / verificação de seguimento de ragras / acertos 
            print("você não chutou um número entre 0 à 100")
            
            continue 
        if chute < x :
            print("chute um número maior")
        elif chute > x: 
            print("chte um número menor") 
        else:
            print("você acertou! ")
            break
    if x != chute:
        print("você perdeu. jogue novamente!")
    print("sua pontuação foi de {}".format(pontos))        
    print("fim do jogo.")


if(__name__=="__main__"):
    jogo()


#testando pro git
#testando mais uma vez 
